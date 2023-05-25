from PyQt5.QtWidgets import QApplication, QCalendarWidget, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QDate, Qt

class CalendarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.calendar = QCalendarWidget(self)
        self.calendar.selectionChanged.connect(self.show_days_since_today)

        self.days_label = QLabel(self)
        self.weeks_label = QLabel(self)
        self.years_label = QLabel(self)
        self.leap_years_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.days_label)
        layout.addWidget(self.weeks_label)
        layout.addWidget(self.years_label)
        layout.addWidget(self.leap_years_label)
        self.setLayout(layout)

        self.show_days_since_today()

    def show_days_since_today(self):
        selected_date = self.calendar.selectedDate()
        today = QDate.currentDate()

        days_diff = today.daysTo(selected_date)
        weeks_diff = int(days_diff / 7)
        years_diff = today.daysTo(selected_date) / 365.25
        leap_years = sum(1 for year in range(today.year(), selected_date.year()+1) if QDate.isLeapYear(year))

        self.days_label.setText(f"Days since today: {days_diff}")
        self.weeks_label.setText(f"Weeks since today: {weeks_diff}")
        self.years_label.setText(f"Years since today: {years_diff:.2f}")
        self.leap_years_label.setText(f"Leap years in the range: {leap_years}")

if __name__ == '__main__':
    app = QApplication([])
    calendar_widget = CalendarWidget()
    calendar_widget.show()
    app.exec_()
