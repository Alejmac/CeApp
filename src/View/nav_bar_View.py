import flet as ft
from flet import CupertinoNavigationBar, NavigationDestination, icons

def create_nav_bar(main_instance):
    nav_bar = CupertinoNavigationBar(
        destinations=[
            NavigationDestination(
                icon=icons.SCHEDULE,
                label="Schedule"
            ),
            NavigationDestination(
                icon=icons.CALENDAR_VIEW_MONTH,
                label="Data Student"
            ),
            NavigationDestination(
                icon=icons.CALENDAR_VIEW_DAY,
                label="Login"
            )
        ],
        on_change=lambda e: handle_navigation(e, main_instance),
    )

    return nav_bar

def handle_navigation(e, main_instance):
    selected_index = e.control.selected_index
    main_instance.on_nav_click(selected_index)