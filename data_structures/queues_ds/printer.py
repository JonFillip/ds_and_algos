class Printer:
    """Simulates the attributes and functions of a printers task."""
    def __init__(self, ppm):
        """Initialize the attributes."""
        self.print_rate = ppm  # Stands for pages printed per minute
        self.current_task = None  # Checks if the printer has a current task
        self.time_left = 0  # time left for current task

    def timer(self):
        """Decrements the internal timer and sets the printer to idle if the
        task is completed."""
        if self.current_task is not None:
            self.time_left -= 1
            if self.time_left <= 0:
                self.current_task = None

    def in_use(self):
        """Use status of the printer."""
        if self.current_task is not None:
            return True
        else:
            return False

    def start_task(self, new_task):
        self.current_task = new_task
        self.time_left = new_task.get_pages() * 60 / self.print_rate
