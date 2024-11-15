import flet as ft
import asyncio

class Countdown(ft.Text):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1



def main(page: ft.Page):
    page.title = "Async Countdown"
    page.update()

    #Create three timers with different initial values, one per each tab
    timers=[Countdown(20), Countdown(30), Countdown(40)]
    selectedTimer = 0

    # Define UI elements for each timer
    timer_controls = []
    for i, timer in enumerate(timers):
        # Define the text that displays the remaining time
        remainingTime = ft.Text(f"Remaining Time: {timer.seconds}s", size=20)

        # Define a progress bar for each timer
        progressBar = ft.Progress(value=0)

        # Define the buttons for each timer
        startBtn = ft.Button("Start", on_click=lambda e: startCountdown())
        pauseBtn = ft.Button("Pause", on_click=lambda e: pauseCountdown())
        resetBtn = ft.Button("Reset", on_click=lambda e: resetCountdown())

        timer_controls.append(
            ft.Column([
                ft.Text(f"Timer {i+1}", size=25),
                remainingTime,
                progressBar,
                ft.Row([startBtn, pauseBtn, resetBtn], alignment=ft.MainAxisAlignment.CENTER),
            ])
        )

    

    def startCountdown(index):
        timers[index].start()
        page.run_task(updateTimerDisplay)

    def pauseCountdown(index):
        timers[index].pause()
        page.run_task(updateTimerDisplay)
    
    def resetCountdown(index):
        timers[index].reset()
        page.run_task(updateTimerDisplay)
    
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Timer 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Timer 1",
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Timer 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )

    # Display the selected timer
    def showTimers(index):
        nonlocal selectedTimer
        selectedTimer = index
        page.clear()
        page.controls.append(timer_controls[selectedTimer])
        page.update()

ft.app(main)