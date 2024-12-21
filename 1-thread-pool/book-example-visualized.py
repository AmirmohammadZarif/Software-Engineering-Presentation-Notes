from manim import *

class ThreadPoolVisualization(Scene):
    def construct(self):
        # Configuration
        n_threads = 4
        n_tasks = 8
        
        # Create thread pool title
        title = Text("Thread Pool Executor", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # Create task queue
        queue_box = Rectangle(height=5, width=2, color=WHITE)
        queue_label = Text("Task Queue", font_size=24)
        queue_group = VGroup(queue_box, queue_label).arrange(DOWN, buff=0.5)
        queue_group.to_edge(LEFT, buff=2)
        
        # Create tasks in queue
        task_boxes = VGroup(*[
            VGroup(
                Rectangle(height=0.4, width=1.2, fill_color=BLUE, fill_opacity=0.5),
                Text(f"Task {i}", font_size=16)
            ).arrange(buff=0.1)
            for i in range(n_tasks)
        ]).arrange(DOWN, buff=0.2)
        task_boxes.move_to(queue_box)
        
        # Create thread lanes
        threads = VGroup(*[
            VGroup(
                Rectangle(height=0.6, width=6, color=WHITE),
                Text(f"Thread {i+1}", font_size=20)
            ).arrange(buff=0.5)
            for i in range(n_threads)
        ]).arrange(DOWN, buff=0.3)
        threads.next_to(queue_group, RIGHT, buff=1)
        
        # Center the entire visualization
        whole_scene = VGroup(queue_group, threads)
        whole_scene.center()
        
        # Setup initial scene
        self.play(
            Create(queue_box),
            Write(queue_label),
            Create(threads),
            Create(task_boxes)
        )
        
        # Simulate thread pool execution
        running_tasks = []
        available_threads = list(range(n_threads))
        
        # Process tasks
        for task_idx in range(n_tasks):
            # Wait if no threads available
            if not available_threads:
                self.wait(0.5)
                # Complete a random running task
                completed_idx = len(running_tasks) - 1
                completed_task = running_tasks.pop(completed_idx)
                thread_idx = completed_task[1]
                available_threads.append(thread_idx)
                self.play(
                    FadeOut(completed_task[0]),
                    run_time=0.5
                )
            
            # Get next task and available thread
            task = task_boxes[task_idx]
            thread_idx = available_threads.pop(0)
            
            # Show task being taken from queue
            task_copy = task.copy()
            
            # Animate task assignment
            self.play(
                task.animate.set_opacity(0.2),
                task_copy.animate.next_to(threads[thread_idx][0], RIGHT, buff=0.2),
                run_time=0.5
            )
            
            # Show task processing
            progress_bar = Rectangle(
                height=0.3,
                width=0,
                fill_color=GREEN,
                fill_opacity=0.5
            ).next_to(task_copy, RIGHT, buff=0.1)
            
            self.play(
                Create(progress_bar),
                progress_bar.animate.set_width(1.5),
                run_time=1
            )
            
            # Add to running tasks
            running_tasks.append((task_copy, thread_idx))
        
        # Complete remaining tasks
        for task, thread_idx in running_tasks:
            self.play(FadeOut(task), run_time=0.5)
            available_threads.append(thread_idx)
        
        self.wait(1)
        
        # Show completion
        completion_text = Text("All tasks completed!", color=GREEN, font_size=32)
        completion_text.next_to(title, DOWN)
        self.play(Write(completion_text))
        self.wait(2)