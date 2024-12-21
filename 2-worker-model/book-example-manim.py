from manim import *
import numpy as np

class DeliverySystemVisualization(Scene):
    def construct(self):
        # Configuration
        NUM_WORKERS = 4
        NUM_PACKAGES = 10
        
        # Create title
        title = Text("Package Delivery System", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Create worker progress bars
        worker_groups = []
        for i in range(NUM_WORKERS):
            # Worker label
            worker_label = Text(f"Worker {i}", font_size=24)
            
            # Progress bar background
            bar_bg = Rectangle(
                width=6,
                height=0.3,
                fill_opacity=0.2,
                color=GRAY
            )
            
            # Progress bar fill (starts empty)
            bar_fill = Rectangle(
                width=0,
                height=0.3,
                fill_opacity=1,
                color=BLUE
            )
            bar_fill.align_to(bar_bg, LEFT)
            
            # Package label
            package_label = Text("IDLE", font_size=20, color=GRAY)
            package_label.next_to(bar_bg, RIGHT)
            
            # Group elements
            group = VGroup(worker_label, bar_bg, bar_fill, package_label)
            group.arrange(RIGHT, buff=0.5)
            worker_groups.append({
                'group': group,
                'bar_fill': bar_fill,
                'package_label': package_label,
                'active': False
            })

        # Arrange worker groups vertically
        VGroup(*[g['group'] for g in worker_groups]).arrange(
            DOWN, buff=0.5
        ).shift(DOWN)

        # Show initial state
        self.play(
            *[FadeIn(g['group']) for g in worker_groups]
        )

        # Simulate deliveries
        delivery_data = self.generate_delivery_data(NUM_WORKERS, NUM_PACKAGES)
        
        # Animate deliveries
        self.animate_deliveries(worker_groups, delivery_data)
        
        # Show completion message
        completion = Text("All packages delivered! 🎉", font_size=36, color=GREEN)
        completion.next_to(VGroup(*[g['group'] for g in worker_groups]), DOWN, buff=1)
        self.play(Write(completion))
        self.wait(2)

    def generate_delivery_data(self, num_workers, num_packages):
        # Simulate delivery assignments and progress
        # Returns a list of (worker_id, package_id, progress) tuples
        data = []
        current_time = 0
        packages_left = list(range(num_packages))
        worker_status = {i: None for i in range(num_workers)}
        
        while packages_left or any(status is not None for status in worker_status.values()):
            # Assign packages to idle workers
            for worker_id, status in worker_status.items():
                if status is None and packages_left:
                    package_id = packages_left.pop(0)
                    duration = np.random.uniform(2, 4)
                    worker_status[worker_id] = (package_id, current_time, duration)
            
            # Record progress
            for worker_id, status in worker_status.items():
                if status is not None:
                    package_id, start_time, duration = status
                    progress = (current_time - start_time) / duration
                    if progress >= 1:
                        worker_status[worker_id] = None
                    else:
                        data.append((worker_id, package_id, progress))
            
            current_time += 0.1
            
        return data

    def animate_deliveries(self, worker_groups, delivery_data):
        # Group updates by time step
        current_updates = []
        worker_current_package = {i: None for i in range(len(worker_groups))}  # Track current package
        
        for i, (worker_id, package_id, progress) in enumerate(delivery_data):
            current_updates.append((worker_id, package_id, progress))
            
            # Apply updates every few frames or at the end
            if i == len(delivery_data) - 1 or len(current_updates) >= len(worker_groups):
                animations = []
                
                for w_id, p_id, prog in current_updates:
                    worker = worker_groups[w_id]
                    bar_fill = worker['bar_fill']
                    bg_bar = worker['group'][1]  # Background bar
                    
                    # Calculate new width and position
                    new_width = 6 * prog
                    new_bar = Rectangle(
                        width=new_width,
                        height=0.3,
                        fill_opacity=1,
                        color=BLUE
                    ).move_to(bar_fill)
                    new_bar.align_to(bg_bar, LEFT)
                    
                    # Check if package changed or progress complete
                    if worker_current_package[w_id] != p_id or prog >= 0.99:
                        worker_current_package[w_id] = p_id
                        package_text = "IDLE" if prog >= 0.99 else f"Package {p_id}"
                        package_color = GRAY if prog >= 0.99 else WHITE
                        
                        animations.extend([
                            Transform(bar_fill, new_bar),
                            worker['package_label'].animate.become(
                                Text(package_text, font_size=20, color=package_color).move_to(
                                    worker['package_label']
                                )
                            )
                        ])
                    else:
                        # Just update progress
                        animations.append(Transform(bar_fill, new_bar))
                
                if animations:
                    self.play(*animations, run_time=0.1)
                current_updates = []