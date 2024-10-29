import flet as ft
from flet import NavigationBar, NavigationDestination, icons

def create_nav_bar(page):
    nav_bar = ft.CupertinoNavigationBar(
        destinations=[
            NavigationDestination(
                icon=icons.SCHEDULE,
                
            ),
            NavigationDestination(
                icon=icons.CALENDAR_VIEW_MONTH,
                
            ),
            NavigationDestination(
                icon=icons.CALENDAR_VIEW_DAY,
                
            )
        ],
        on_change=lambda e: handle_navigation(e, page),
        
    )

    return nav_bar

def handle_navigation(e, page):
    selected_index = e.control.selected_index
    if selected_index == 0:
        print("Schedule clicked")
    elif selected_index == 1:
        print("Calendar clicked")
    elif selected_index == 2:
        print("Day View clicked")