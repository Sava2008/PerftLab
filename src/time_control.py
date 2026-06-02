class TimeControl:
    def __init__(
        self, hours: int, minutes: int, seconds: int, increment_secs: float
    ) -> None:
        if seconds > 59 or minutes > 59 or hours > 3:
            raise ValueError("bad time constraints")

        self.start_hours: int = hours
        self.start_mins: int = minutes
        self.start_secs: int = seconds
        self.increment: float = increment_secs
        self.time_as_secs: float = hours * 60 * 60 + minutes * 60 + seconds

    def apply_increment(self) -> None:
        self.time_as_secs += self.increment

    def decrease_time(self, decrease_as_secs: float) -> None:
        self.time_as_secs -= decrease_as_secs

    def convert_to_pgn_time(self) -> str:
        minutes_pgn: float = (
            self.start_hours * 60 + self.start_mins + self.start_secs / 60
        )
        int_minutes: int = int(minutes_pgn)
        if minutes_pgn == int_minutes:
            minutes_pgn = int_minutes
        return f"{minutes_pgn}+{self.increment}"
