import os
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.video import Video
from kivymd.app import MDApp
import webbrowser
import requests
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.button import MDButton, MDButtonText, MDFabButton
from kivymd.uix.dialog import MDDialog, MDDialogButtonContainer, MDDialogContentContainer, MDDialogHeadlineText, MDDialogIcon, MDDialogSupportingText
from kivymd.uix.widget import Widget
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu
os.environ["KIVY_VIDEO"] = "ffpyplayer"
UI = """
MDNavigationLayout:
    MDScreenManager:
        id: sm
        MDScreen:
            name: 'splash'
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(30)
                padding: dp(30)
                Widget:
    
                MDCard:
                    id: logo_card
                    size_hint: None, None
                    size: dp(100), dp(100)
                    pos_hint: {"center_y":.5, "center_x":.5}
                    radius: [18, 18, 18, 18]
                    FitImage:
                        source: "itrendlogo.png"
                        size_hint: None, None
                        size: logo_card.size
                        radius: logo_card.radius
                        pos_hint: {"center_x":.5, "center_y":.5}
                    Widget:
                        size_hint_y: None
                        height: dp(30)
                MDCircularProgressIndicator:
                    size_hint: None, None
                    size: dp(48), dp(48)
                    pos_hint: {"center_x":.5, "center_y":.2}
                Widget:
                MDLabel:
                    text: "from NEPTUNE DEV."
                    size_hint_y: None
                    height: dp(35)
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "white"
                Widget:
                    size_hint_y: None
                    height: dp(30)
        MDScreen:
            name: "home"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(40)
                    padding: dp(10)
                    MDIconButton:
                        icon: "menu"
                        size_hint_x: .1
                        on_release: nav_drawer.set_state("toggle")
                    Widget:
                        size_hint_x: .8
                    MDIconButton: 
                        id: account_info
                        icon: "account-circle-outline"
                        size_hint_x: .1
                        on_release: app.account_info()
                MDScrollView:
                    MDGridLayout:
                        cols: 1
                        padding: dp(10)
                        id: content_container
        MDScreen:
            name: "topic_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "home"
                    Widget:
                MDScrollView:
                    MDGridLayout:
                        cols: 1
                        spacing: dp(28)
                        padding: dp(10)
                        id: topic_content
        MDScreen:
            name: "account_screen"
            id: account_screen
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "home"
                    Widget:
                Widget:
                    size_hint_y: None
                    height: dp(20)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(2.5)
                    padding: dp(10)
                    orientation: "vertical"
                    MDLabel:
                        id: account_name
                        text: " "
                        size_hint_y: None
                        adaptive_height: True
                        halign: "center"
                        valign: "top"
                        theme_font_size: "Custom"
                        font_size: sp(32)
                        theme_text_color: "Custom"
                        text_color: "yellow"
                        theme_font_name: "Custom"
                        font_name: "heading_font.ttf"
                    MDLabel:
                        id: account_email
                        text: " "
                        size_hint_y: None
                        adaptive_height: True
                        halign: "center"
                        valign: "top"
                        theme_font_size: "Custom"
                        font_size: sp(18)
                        theme_text_color: "Custom"
                        text_color: "yellow"
                        theme_font_name: "Custom"
                        font_name: "Montserrat-Bold.ttf"
                Widget:
                    size_hint_y: None
                    height: dp(20)
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(20)
                    padding: dp(10)
                    id: account_features
                    MDButton:
                        on_release: app.show_favorites()
                        pos_hint: {"center_x":.5}
                        size_hint_x: .8
                        MDButtonText:
                            text: "My Favorites"
                        MDButtonIcon:
                            icon: "star-outline"
                    MDButton:
                        on_release: app.logout()
                        pos_hint: {"center_x":.5}
                        size_hint_x: .8
                        MDButtonText:
                            text: "Sign Out"
                        MDButtonIcon:
                            icon: "logout"
                Widget:
                
        MDScreen:
            name: "favorites_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "account_screen"
                    Widget:
                MDScrollView:
                    MDGridLayout:
                        id: favorites_container
                        cols: 1
                        padding: dp(10)
                        spacing: dp(10)

        MDScreen:
            name: "fav_topic_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "favorites_screen"
                    Widget:
                MDScrollView:
                    MDGridLayout:
                        cols: 1
                        spacing: dp(28)
                        padding: dp(10)
                        id: fav_topic_content
        
        MDScreen:
            name: "about_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "home"
                    Widget:
                Widget:
                    size_hint_y: None
                    height: dp(20)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(2.5)
                    padding: dp(10)
                    orientation: "vertical"
                    MDLabel:
                        text: "iTREND"
                        size_hint_y: None
                        adaptive_height: True
                        halign: "center"
                        valign: "top"
                        theme_font_size: "Custom"
                        font_size: sp(32)
                        theme_text_color: "Custom"
                        text_color: "yellow"
                        theme_font_name: "Custom"
                        font_name: "heading_font.ttf"
                    MDLabel:
                        text: "About Us"
                        size_hint_y: None
                        adaptive_height: True
                        halign: "center"
                        valign: "top"
                        theme_font_size: "Custom"
                        font_size: sp(18)
                        theme_text_color: "Custom"
                        text_color: "yellow"
                        theme_font_name: "Custom"
                        font_name: "Montserrat-Bold.ttf"
                Widget:
                    size_hint_y: None
                    height: dp(20)
                MDGridLayout:
                    cols: 2
                    spacing: dp(16)
                    padding: dp(5)
                    id: account_features
                    MDLabel:
                        text: "Version: "
                        halign: "center"
                        size_hint_y: None
                        height: dp(40)
                    MDLabel:
                        text: "1.0.0"
                        halign: "center"
                        size_hint_y: None
                        height: dp(40)
                    MDLabel:
                        text: "Developer: "
                        halign: "center"
                        size_hint_y: None
                        height: dp(40)
                    MDLabel:
                        text: "Fidel Castro(King)"
                        halign: "center"
                        size_hint_y: None
                        height: dp(40)
                    MDLabel:
                        text: "Copyright: "
                        halign: "center"
                        size_hint_y: None
                        height: dp(40)
                    MDLabel:
                        text: "neptune developers"
                        halign: "center"
                        size_hint_y: None
                        height: dp(40)
                MDGridLayout:
                    cols: 7
                    spacing: dp(7)
                    Widget:
                    MDFabButton:
                        icon: "facebook"
                        theme_icon_color: "Custom"
                        icon_color: "blue"
                        on_release: app.open_website("https://www.facebook.com/were castro/")
                    MDFabButton:
                        icon: "instagram"
                        theme_icon_color: "Custom"
                        icon_color: "magenta"
                        on_release: app.open_website("https://www.instagram.com/de_l.fi/")
                    MDFabButton:
                        icon: "whatsapp"
                        theme_icon_color: "Custom"
                        icon_color: "green"
                        on_release: app.open_website("https://wa.me/254737841451")
                    MDFabButton:
                        icon: "github"
                        theme_icon_color: "Custom"
                        icon_color: "grey"
                        on_release: app.open_website("https://github.com/b100mBUG")
                    MDFabButton:
                        icon: "twitter"
                        theme_icon_color: "Custom"
                        icon_color: "cyan"
                    Widget:
                    
        MDScreen:
            name: "video_view"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    id: the_toolbar
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: 
                            sm.current = "home"
                            my_video.state = "stop"
                    Widget:
                        size_hint_y: None
                        height: dp(30)
                Widget:
                    size_hint_y: None
                    height: dp(30)
                MDRelativeLayout:
                    Video:
                        id: my_video
                        source: ""
                        state: "pause"
                        pos_hint: {"center_x":.5, "center_y":.5}
                        size_hint: 1, 1
                        keep_ratio: True
                        allow_stretch: True
                        on_touch_down: app.toggle_controls(*args)
                    MDIconButton:
                        id: play_pause_button
                        icon: "pause"
                        pos_hint: {"center_x":.5, "center_y":.5}
                        theme_icon_color: "Custom"
                        icon_color: "magenta"
                        theme_bg_color: "Custom"
                        md_bg_color: "white"
                        opacity: 1
                        on_release: app.play_pause()
                    MDSlider:
                        id: slider
                        min: 0
                        max: 100
                        value: 50
                        track_color: (1, 0, 1, 1)  
                        active_color: (1, 0, 1, 1)
                        thumb_color: (1, 0, 1, 1) 
                        pos_hint: {"center_x": .5, "center_y": .35}
                        opacity: 1
                        size_hint: .7, .15
        MDScreen:
            name: "comment_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    spacing: dp(10)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "home"
                    Widget:
                MDLabel:
                    id: comment_label
                    text: "comment section"
                    size_hint_y: None
                    height: dp(40)
                    halign: "center"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: "yellow"
                    theme_font_size: "Custom"
                    font_size: sp(26)
                MDScrollView:
                    MDGridLayout:
                        cols: 1
                        spacing: dp(10)
                        padding: dp(8)
                        id: comment_container
                MDBoxLayout:
                    id: comment_actions
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(10)
                    
    MDNavigationDrawer:
        id: nav_drawer
        radius: 0, dp(16), dp(16), 0
        theme_bg_color: "Custom"
        md_bg_color: 0.796, 0.765, 0.89, 1
        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(15)
            FitImage:
                source: "itrendlogo.png"
                radius: [16, 16, 16, 16]
            MDLabel:
                text: "iTREND dashboard"
                size_hint_y: None
                height: dp(30)
                bold: True
                theme_font_name: "Custom"
                font_name: "Montserrat-Bold.ttf"
                theme_text_color: "Custom"
                text_color: "blue"
            MDScrollView:
                MDList:
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: 0.796, 0.765, 0.89, 1
                        on_release: app.account_screen()
                        MDListItemLeadingIcon:
                            icon: "account"
                            theme_icon_color: "Custom"
                            icon_color: "magenta"
                        MDListItemHeadlineText:
                            text: "Account"
                            theme_font_name: "Custom"
                            font_name: "Montserrat-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: "blue"
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: 0.796, 0.765, 0.89, 1
                        on_release: app.favorites_screen()
                        MDListItemLeadingIcon:
                            icon: "star-outline"
                            theme_icon_color: "Custom"
                            icon_color: "magenta"
                        MDListItemHeadlineText:
                            text: "Favorites"
                            theme_font_name: "Custom"
                            font_name: "Montserrat-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: "blue"
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: 0.796, 0.765, 0.89, 1
                        on_release: app.explore_content()
                        MDListItemLeadingIcon:
                            icon: "compass-outline"
                            theme_icon_color: "Custom"
                            icon_color: "magenta"
                        MDListItemHeadlineText:
                            text: "Explore"
                            theme_font_name: "Custom"
                            font_name: "Montserrat-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: "blue"
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: 0.796, 0.765, 0.89, 1
                        MDListItemLeadingIcon:
                            icon: "magnify"
                            theme_icon_color: "Custom"
                            icon_color: "magenta"
                        MDListItemHeadlineText:
                            text: "Quick Search"
                            theme_font_name: "Custom"
                            font_name: "Montserrat-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: "blue"
            MDList:
                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: 0.796, 0.765, 0.89, 1
                    MDListItemLeadingIcon:
                        icon: "heart"
                        theme_icon_color: "Custom"
                        icon_color: "magenta"
                    MDListItemHeadlineText:
                        text: "Donate"
                        theme_font_name: "Custom"
                        font_name: "Montserrat-Bold.ttf"
                        theme_text_color: "Custom"
                        text_color: "blue"
                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: 0.796, 0.765, 0.89, 1
                    on_release: app.view_about()
                    MDListItemLeadingIcon:
                        icon: "information-outline"
                        theme_icon_color: "Custom"
                        icon_color: "magenta"
                    MDListItemHeadlineText:
                        text: "About iTREND"
                        theme_font_name: "Custom"
                        font_name: "Montserrat-Bold.ttf"
                        theme_text_color: "Custom"
                        text_color: "blue"
        
            
"""
Window.size = (385, 650)
class iTREND(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Magenta"
        return Builder.load_string(UI)

    def on_start(self):
        self.signedin = False
        Clock.schedule_once(self.go_to_home, 10)
        self.add_content()

    def go_to_home(self, *args):
        self.root.ids.sm.current = 'home'
    def add_content(self, *args):
        url = "http://192.168.100.36:8000/topics/"
        topics = requests.get(url).json()
        self.grid = self.root.ids.content_container
        self.grid.clear_widgets()
        self.grid.size_hint_y = None
        self.grid.bind(minimum_height = self.grid.setter("height"))
        for topic in topics:
            self.heading = topic["Title"]
            self.illustration = topic["Desc"]
            self.media = topic["Media"]
            self.likes = topic["Likes"]
            self.dislikes = topic["Dislikes"]
            self.shares = topic["Shares"]
            self.favorites = topic["Favorites"]
            self.reports = topic["Reports"]
            self.comment_count = topic["Comments"]
            content = f"\n{self.heading}\n{self.illustration}\n\t\t{self.media}\t\t\n\t\t{self.likes} Likes  {self.dislikes} Dislikes  {self.shares} Shares  {self.favorites} Favorites {self.reports} Reports"
            heading_title = MDLabel(
                        text = self.heading,
                        size_hint_y = None,
                        height = dp(40),
                        pos_hint = {"y":.9},
                        theme_font_size = "Custom",
                        font_size = sp(22),
                        valign = "top",
                        bold = True,
                        theme_text_color = "Custom",
                        text_color = "yellow",
                        theme_font_name = "Custom",
                        font_name = "Montserrat-Bold.ttf"

                    )
            heading_title.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
            paragraph = MDLabel(
                    text = f"{self.illustration[:109]} ...",
                    max_lines = 1,
                    ellipsis_options = {"mode": "end"},
                    halign = "left",
                    pos_hint = {"y":.69},
                    valign = "top",
                    size_hint_y = None,
                    theme_text_color = "Custom",
                    text_color = "white",
                    theme_font_name = "Custom",
                    font_name = "Traffolight.otf",
                    height = dp(20)
                )
            paragraph.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
            cont_layout = MDRelativeLayout()
            cont_layout.add_widget(heading_title)
            cont_layout.add_widget(paragraph)
            video = Video(
                source=self.media,
                state="play",
                volume = 0,
                size_hint_y=None,
                height=dp(150),
                size_hint_x=0.95,
                pos_hint={"center_y": .25, "center_x": .5}
            )
            cont_layout.add_widget(
                video,
            )
            content_card = MDCard(
                cont_layout,
                size_hint_y = None,
                height = dp(300),
                padding = dp(20),
                radius = [18, 18, 0, 0],
                style = "outlined",
                theme_bg_color = "Custom",
                md_bg_color = [0, 1, 1, .2],
                on_release = lambda instance, topic_title = self.heading, topic_desc = self.illustration, topic_media = self.media: self.view_content(topic_title, topic_desc, topic_media)
            )
            feedback_card = MDCard(
                MDRelativeLayout(
                    MDIconButton(
                        icon = "thumb-up",
                        pos_hint = {"center_y":.5, "center_x":.059},
                        size_hint_x = 0.2,
                        padding = dp(5),
                        on_release = lambda btn, title = self.heading: self.like_topic(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.likes}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.125},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "thumb-down",
                        pos_hint = {"center_y":.5, "center_x":.225},
                        size_hint_x = 0.2,
                        on_release = lambda btn, title = self.heading: self.dislike_topic(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.dislikes}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.291},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "message",
                        pos_hint = {"center_y":.5, "center_x":.391},
                        size_hint_x = 0.2,
                        on_release = lambda btn, title = self.heading: self.open_comments_card(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.comment_count}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.457},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "share",
                        pos_hint = {"center_y":.5, "center_x":.557},
                        size_hint_x = 0.2,
                    ),
                    MDLabel(
                        text = str(f"  {self.shares}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.623},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "star-outline",
                        pos_hint = {"center_y":.5, "center_x":.723},
                        size_hint_x = 0.2,
                        on_release = lambda btn, title = self.heading: self.favorite_topic(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.favorites}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.789},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "cancel",
                        pos_hint = {"center_y":.5, "center_x": .889},
                        size_hint_x = 0.2,
                        on_release = lambda btn, title = self.heading: self.report_topic(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.reports}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.965},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                ),
                size_hint_y = None,
                height = dp(40),
                radius = [0, 0, 18, 18],
                style = "outlined",
                theme_bg_color = "Custom",
                md_bg_color = [0, 1, 1, .4]
            )
            space = Widget(
                size_hint_y = None,
                height = dp(20)

            )
            self.grid.add_widget(content_card)
            self.grid.add_widget(feedback_card)
            self.grid.add_widget(space)
    def account_info(self):
        if not hasattr(self, 'account_menu') or not self.account_menu:
            account_items = [
                {
                    "text": "Sign In",
                    "theme_text_color": "Custom",
                    "text_color": [0, 0, .6, 1],
                    "leading_icon": "account",
                    "theme_leading_icon_color": "Custom",
                    "leading_icon_color": [0, 0, .6, 1],
                    "on_release": self.go_to_login
                },
                {
                    "text": "Register",
                    "leading_icon": "account-plus",
                    "theme_text_color": "Custom",
                    "text_color": [0, 0, .6, 1],
                    "theme_leading_icon_color": "Custom",
                    "leading_icon_color": [0, 0, .6, 1],
                    "on_release": self.open_signup_dialog
                }
            ]
            self.signin_signup_menu =  MDDropdownMenu(
                caller = self.root.ids.account_info,
                items = account_items
            )
            self.account_menu = self.signin_signup_menu
        self.account_menu.open()

    def close_account_menu(self, *args):
        if self.account_menu:
            self.account_menu.dismiss()  # Dismiss the dialog
            self.account_menu = None

    def go_to_login(self):
        self.close_account_menu()
        self.open_login_dialog()

    def open_login_dialog(self):
        if not hasattr(self, 'login_dialog') or not self.login_dialog:
            self.signin_username = MDTextField(
                MDTextFieldHintText(text="Username")
            )
            self.signin_password = MDTextField(
                MDTextFieldHintText(text="Password"),
                password = True
            )

            self.signin_validator = MDLabel(
                text = " ",
                theme_text_color = "Custom",
                text_color = "red"
            )

            content = MDDialogContentContainer(orientation="vertical", spacing=dp(20))
            content.add_widget(self.signin_username)
            content.add_widget(self.signin_password)
            content.add_widget(self.signin_validator)

            self.login_dialog = MDDialog(
                MDDialogIcon(icon="account"),
                MDDialogHeadlineText(text="Login to your account"),
                MDDialogSupportingText(text="Enter the username and password below"),
                content,
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="Sign In"),
                        on_release=lambda x: self.signin()
                    ),
                    MDButton(
                        MDButtonText(text="Cancel"),
                        on_release=lambda x: self.close_login_dialog()
                    ),
                    spacing=dp(15)
                )
            )

        self.login_dialog.open()

    def close_login_dialog(self):
        if self.login_dialog:
            self.login_dialog.dismiss()  # Dismiss the dialog
            self.login_dialog = None    # Clear the reference to allow re-creation

    def open_signup_dialog(self):
        self.close_account_menu()
        if not hasattr(self, 'signup_dialog') or not self.signup_dialog:
            self.register_username = MDTextField(
                MDTextFieldHintText(text = "Set username")
            )
            self.register_email = MDTextField(
                MDTextFieldHintText(text = "Email")
            )
            self.register_password = MDTextField(
                MDTextFieldHintText(text = "Set password"),
                password = True
            )
            self.register_password_confirm = MDTextField(
                MDTextFieldHintText(text = "Confirm password"),
                password = True
            )
            self.register_gender = MDTextField(
                MDTextFieldHintText(text = "Gender")
            )
            self.signup_validator = MDLabel(
                text = " ",
                theme_text_color = "Custom",
                text_color = "red"
            )
            content = MDDialogContentContainer(orientation = "vertical", spacing = dp(20))
            content.add_widget(self.register_username)
            content.add_widget(self.register_email)
            content.add_widget(self.register_password)
            content.add_widget(self.register_password_confirm)
            content.add_widget(self.register_gender)
            content.add_widget(self.signup_validator)
            self.signup_dialog = MDDialog(
                MDDialogIcon(icon = "account-plus"),
                MDDialogHeadlineText(text = "Create an iTREND account"),
                MDDialogSupportingText(text = "Enter your credentials as below"),
                content,
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text = "Register"),
                        on_release = self.register
                    ),
                    MDButton(
                        MDButtonText(text = "Cancel"),
                        on_release = self.close_signup_dialog
                    ),
                    spacing = dp(15)
                )
            )
        self.signup_dialog.open()

    def close_signup_dialog(self, *args):
        if self.signup_dialog:
            self.signup_dialog.dismiss()
            self.signup_dialog = None

    def signin(self, *args):
        self.username = self.signin_username.text
        self.password = self.signin_password.text
        url = "http://192.168.100.36:8000/viewers/"
        viewers = requests.get(url).json()
        stored_user = ""
        for viewer in viewers:
            if viewer["Name"] == self.username:
                stored_user = viewer
                break
        if stored_user:
            if self.password == stored_user["Password"]:
                self.open_welcome_dialog()
                self.signedin = True
                self.root.ids.account_info.on_release = self.show_signed_in_account
                return
            else:
                self.signin_validator.text = "Incorrect Password. Try again."
        else:
            self.signin_validator.text = f"<{self.username}> does not exist. Try different username"
    def show_signed_in_account(self, *kwargs):
        self.account_menu.dismiss()
        if not hasattr(self, 'signin_menu') or not self.signin_menu:
            sigin_menu = [
                        {"text": self.username,
                        "theme_text_color": "Custom",
                        "text_color": [0, 0, .6, 1],
                        "leading_icon": "account",
                        "theme_leading_icon_color": "Custom",
                        "leading_icon_color": [0, 0, .6, 1],
                        "on_release": self.initialize_account
                        }
                    ]
            self.signin_menu =  MDDropdownMenu(
                    caller = self.root.ids.account_info,
                    items = sigin_menu
                )
        self.new_menu = self.signin_menu
        self.new_menu.open()
    def close_new_account_menu(self, *args):
        if self.signin_menu:
            self.signin_menu.dismiss()
            self.signin_menu = None
    def initialize_account(self):
        self.close_new_account_menu()
        self.go_to_account()
    def go_to_account(self, *args):
        url = "http://192.168.100.36:8000/get%20user/"
        stored_user = requests.get(f"{url}{self.username}").json()
        self.root.ids.sm.current = "account_screen"
        self.root.ids.account_name.text = stored_user["Name"]
        self.root.ids.account_email.text = stored_user["Email"]
        self.root.ids.account_name.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        self.root.ids.account_email.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
    def register(self, *args):
        self.my_username = self.register_username.text
        email = self.register_email.text
        password = self.register_password.text
        pass_confirm = self.register_password_confirm.text
        gender = self.register_gender.text
        add_url = "http://192.168.100.36:8000/add viewer"
        viewer_url = "http://192.168.100.36:8000/viewers/"
        viewers = requests.get(viewer_url).json()
        existing_user = False
        for viewer in viewers:
            if viewer["Name"] == self.my_username:
                existing_user = True

        if password != pass_confirm:
            self.signup_validator.text = "Passwords do not match! Try re-entering them."
            return
        elif existing_user:
            self.signup_validator.text = "Username already exists. Try something else."
            return
        else:
            data = {
                "viewer_name": self.my_username,
                "viewer_email": email,
                "viewer_password": password,
                "viewer_sex": gender,
                "viewer_interests": "Anything"
            }
            try:
                response = requests.post(add_url, json=data)
                print(response.json())
                self.finish_signup()

            except requests.exceptions.RequestException as e:
                print("Unsuccessful...", e)
                self.signup_validator.text = "Signup failed. Try again"

    def finish_signup(self):
        self.close_signup_dialog()
        self.finish_signup_dialog = MDDialog(
            MDDialogIcon(
                icon = "star-outline"
            ),
            MDDialogHeadlineText(
                text = "Signup Success!"
            ),
            MDDialogSupportingText(
                text = "You can now sign in to your account to access all features"
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(
                        text = "Sign In"
                    ),
                    on_release = self.request_login
                ),
                Widget()
            )
        )
        self.finish_signup_dialog.open()
    def request_login(self, *args):
        self.finish_signup_dialog.dismiss()
        self.open_login_dialog()

    def like_topic(self, title, *args):

        if self.signedin:
            viewer_url = "http://192.168.100.36:8000/viewers/"
            topic_url = "http://192.168.100.36:8000/topics/"
            viewers = requests.get(viewer_url).json()
            topics = requests.get(topic_url).json()
            viewer_username = self.username
            topic_title = title
            for topic in topics:
                if topic["Title"] == topic_title:
                    topic_object = topic
                    break
            for viewer in viewers:
                if viewer["Name"] == viewer_username:
                    viewer_object = viewer
                    break
            like_url = "http://192.168.100.36:8000/like-topic/"
            like_data = {
                "viewer_id": viewer_object["ID"],
                "topic_id": topic_object["ID"]
            }
            Clock.schedule_once(self.add_content, 1)
            response = requests.post(like_url, json=like_data)
            print(response.json())

        else:
            self.open_login_dialog()

    def dislike_topic(self, title, *args):
        if self.signedin:
            viewer_url = "http://192.168.100.36:8000/viewers/"
            topic_url = "http://192.168.100.36:8000/topics/"
            viewers = requests.get(viewer_url).json()
            topics = requests.get(topic_url).json()
            viewer_username = self.username
            topic_title = title
            for topic in topics:
                if topic["Title"] == topic_title:
                    topic_object = topic
                    break
            for viewer in viewers:
                if viewer["Name"] == viewer_username:
                    viewer_object = viewer
                    break
            dislike_url = "http://192.168.100.36:8000/dislike-topic/"
            dislike_data = {
                "viewer_id": viewer_object["ID"],
                "topic_id": topic_object["ID"]
            }
            Clock.schedule_once(self.add_content, 1)
            response = requests.post(dislike_url, json=dislike_data)
            print(response.json())
        else:
            self.open_login_dialog()

    def favorite_topic(self, title, *args):
        if self.signedin:
            viewer_url = "http://192.168.100.36:8000/viewers/"
            topic_url = "http://192.168.100.36:8000/topics/"
            viewers = requests.get(viewer_url).json()
            topics = requests.get(topic_url).json()
            viewer_username = self.username
            topic_title = title
            for topic in topics:
                if topic["Title"] == topic_title:
                    topic_object = topic
                    break
            for viewer in viewers:
                if viewer["Name"] == viewer_username:
                    viewer_object = viewer
                    break
            favorite_url = "http://192.168.100.36:8000/favorite-topic/"
            favorite_data = {
                "viewer_id": viewer_object["ID"],
                "topic_id": topic_object["ID"]
            }
            Clock.schedule_once(self.add_content, 1)
            response = requests.post(favorite_url, json=favorite_data)
            print(response.json())
        else:
            self.open_login_dialog()

    def report_topic(self, title, *args):
        if self.signedin:
            viewer_url = "http://192.168.100.36:8000/viewers/"
            topic_url = "http://192.168.100.36:8000/topics/"
            viewers = requests.get(viewer_url).json()
            topics = requests.get(topic_url).json()
            viewer_username = self.username
            topic_title = title
            for topic in topics:
                if topic["Title"] == topic_title:
                    topic_object = topic
                    break
            for viewer in viewers:
                if viewer["Name"] == viewer_username:
                    viewer_object = viewer
                    break
            report_url = "http://192.168.100.36:8000/report-topic/"
            report_data = {
                "viewer_id": viewer_object["ID"],
                "topic_id": topic_object["ID"]
            }
            Clock.schedule_once(self.add_content, 1)
            response = requests.post(report_url, json=report_data)
            print(response.json())
        else:
            self.open_login_dialog()

    def view_content(self, topic_title, topic_desc, topic_media, *args):
        self.root.ids.sm.current = "topic_screen"
        media_container = MDRelativeLayout(
            size_hint_y = None,
            height = dp(180)
        )
        grid = self.root.ids.topic_content
        grid.size_hint_y = None
        grid.bind(minimum_height = grid.setter("height"))
        grid.clear_widgets()
        title = topic_title.upper()
        article_text = topic_desc
        self.media_url = topic_media

        topic_header = MDLabel(
            text = title,
            halign = "left",
            size_hint_y = None,
            valign = "top",
            adaptive_height = True,
            bold = True,
            theme_font_size = "Custom",
            font_size = sp(18),
            theme_font_name = "Custom",
            font_name = "heading_font.ttf",
            theme_text_color = "Custom",
            text_color = "yellow"
        )
        topic_header.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        article = MDLabel(
            text = article_text,
            size_hint_y = None,
            valign = "top",
            halign = "left",
            theme_text_color = "Custom",
            text_color = [1, 1, 1, 1],
            theme_font_name = "Custom",
            font_name = "times new roman.ttf",
            adaptive_height = True
        )
        article.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        grid.add_widget(topic_header)
        grid.add_widget(article)
        video = Video(
            source=self.media_url,
            state="play",
            volume=0,
            size_hint_y=None,
            height=dp(150),
            size_hint_x = None,
            width = dp(300),
            pos_hint={"center_y": .5, "center_x": .5}
        )
        open_video_button = MDIconButton(
            icon="open-in-new",
            pos_hint={"center_x": .5, "center_y": .5},
            theme_icon_color="Custom",
            icon_color="magenta",
            theme_bg_color="Custom",
            md_bg_color="white",
            on_release=lambda btn: self.video_view(self.media_url)
        )

        media_container.add_widget(video)
        media_container.add_widget(open_video_button)
        grid.add_widget(media_container)
    def video_view(self, media_url):
        self.root.ids.sm.current = "video_view"
        self.root.ids.play_pause_button.icon = "pause"
        self.root.ids.my_video.source = media_url
        self.start_video_playback()

    def play_pause(self):
        video = self.root.ids.my_video
        if video.state == "play":
            video.state = "pause"
            self.root.ids.play_pause_button.icon = "play"
        else:
            video.state = "play"
            self.root.ids.play_pause_button.icon = "pause"
    controls_visible = True
    def toggle_controls(self, instance, touch):
        video = self.root.ids.my_video
        if video.collide_point(*touch.pos):
            self.controls_visible = not self.controls_visible
            opacity = 1 if self.controls_visible else 0
            self.root.ids.play_pause_button.opacity = opacity
            self.root.ids.slider.opacity = opacity
            return True

        return  False

    def start_video_playback(self):
        video = self.root.ids.my_video
        video.state = 'play'
        Clock.schedule_once(self.wait_for_video_ready, 0.5)

    def wait_for_video_ready(self, dt):
        video = self.root.ids.my_video
        if video.duration > 0 and video.position >= 0:
            Clock.schedule_interval(self.update_slider, 0.5)
        else:
            Clock.schedule_once(self.wait_for_video_ready, 0.5)

    def update_slider(self, dt):
        video = self.root.ids.my_video
        if video.duration > 0 and video.position >= 0:
            self.root.ids.slider.max = video.duration
            self.root.ids.slider.value = video.position

    def open_welcome_dialog(self):
        self.close_login_dialog()
        if not hasattr(self, 'welcome_dialog') or not self.welcome_dialog:
            self.welcome_dialog = MDDialog(
                MDDialogIcon(
                    icon = "star",
                ),
                MDDialogHeadlineText(
                    text = f"Hello, {self.username}!"
                ),
                MDDialogSupportingText(
                    text = "Sign In Success. Access all the content features now."
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text = "Okay"),
                        on_release = self.close_welcome_dialog
                    ),
                    Widget()
                )
            )
        self.welcome_dialog.open()
    def close_welcome_dialog(self, *args):
        if self.welcome_dialog:
            self.welcome_dialog.dismiss()
            self.welcome_dialog = None
    def open_comments_card(self, title, *args):
        if self.signedin:
            main_grid = self.root.ids.comment_container
            main_grid.size_hint_y = None
            main_grid.bind(minimum_height=main_grid.setter("height"))
            main_grid.clear_widgets()
            self.root.ids.sm.current = "comment_screen"
            self.comment_text = MDTextField(MDTextFieldHintText(text = "Add comment..."))
            comment_url = "http://192.168.100.36:8000/comments/"
            comment_objects = requests.get(comment_url).json()
            topic_url = "http://192.168.100.36:8000/topics/"
            topic_objects = requests.get(topic_url).json()
            selected_topic = None
            for topic_object in topic_objects:
                if topic_object["Title"] == title:
                    selected_topic = topic_object
                    print(selected_topic)
            self.root.ids.comment_label.text = selected_topic["Title"]
            if not selected_topic:
                print("Topic not found")
                return
            self.comments_validator = MDLabel(
                text = " ",
                size_hint_y = None,
                height = dp(30),
                theme_text_color = "Custom",
                text_color = "red"
            )
            for comment_object in comment_objects:
                if comment_object["Topic"]["topic_title"] == title:
                    commenter = comment_object["Viewer"]["viewer_name"]
                    comment = comment_object["Comment"]
                    viewer = MDLabel(
                        text = commenter,
                        size_hint_y = None,
                        halign = "left",
                        valign = "top",
                        adaptive_height = True,
                        bold = True,
                        theme_font_size = "Custom",
                        font_size = sp(16), 
                        theme_text_color = "Custom",
                        text_color = "blue"

                        )
                    viewer.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
                    text = MDLabel(
                        text = f"   {comment}",
                        size_hint_y = None,
                        halign = "left",
                        valign = "top",
                        adaptive_height = True,
                        theme_text_color = "Custom",
                        text_color = "white"
                        )
                    text.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
                    main_grid.add_widget(viewer)
                    main_grid.add_widget(text)
            action_center = self.root.ids.comment_actions
            action_center.clear_widgets()
            action_center.add_widget(self.comment_text)
            action_center.add_widget(
                MDFabButton(
                    icon = "send",
                    on_release = lambda btn, topic_obj = selected_topic: self.add_comment(topic_obj)
                )
            )
        else:
            self.open_login_dialog()
    def add_comment(self, topic_obj, *args):
        topic_object = topic_obj
        user_url = "http://192.168.100.36:8000/get%20user/"
        viewer_object = requests.get(f"{user_url}{self.username}").json()
        if viewer_object:

            viewer_url = "http://192.168.100.36:8000/viewers/"
            viewers = requests.get(viewer_url).json()
            viewer_username = self.username
            for viewer in viewers:
                if viewer["Name"] == viewer_username:
                    viewer_object = viewer
                    break
            comment_url = "http://192.168.100.36:8000/comment-topic/"
            like_data = {
                "viewer_id": viewer_object["ID"],
                "topic_id": topic_object["ID"],
                "comment": self.comment_text.text
            }
            Clock.schedule_once(self.add_content, 1)
            response = requests.post(comment_url, json=like_data)
            print(topic_object["ID"])
            print(response.json())
            self.comment_text.text = ""

    def show_favorites(self, *args):
        self.root.ids.sm.current = "favorites_screen"
        topics_url = "http://192.168.100.36:8000/favorite_topics/"
        fav_topics = requests.get(topics_url).json()
        self.fav_grid = self.root.ids.favorites_container
        self.fav_grid.size_hint_y = None
        self.fav_grid.bind(minimum_height=self.fav_grid.setter("height"))
        self.fav_grid.clear_widgets()

        for topic in fav_topics:
            if topic["Viewer"]["viewer_name"] == self.username:
                fav_heading = topic["Topic"]["topic_title"]
                fav_illustration = topic["Topic"]["topic_description"]
                fav_media = topic["Topic"]["topic_media_url"]

                cont_layout = MDRelativeLayout()

                heading_title = MDLabel(
                    text=fav_heading,
                    size_hint_y=None,
                    pos_hint={"y": .9},
                    height=dp(40),
                    theme_font_size="Custom",
                    font_size=sp(22),
                    bold=True,
                    valign="top",
                    theme_text_color="Custom",
                    text_color="yellow",
                    theme_font_name="Custom",
                    font_name="Montserrat-Bold.ttf"
                )
                heading_title.bind(width=lambda inst, val: setattr(inst, "text_size", (val, None)))

                paragraph = MDLabel(
                    text=f"{fav_illustration[:109]} ...",
                    halign="left",
                    pos_hint={"y": .69},
                    size_hint_y=None,
                    height=dp(40),
                    valign="top",
                    theme_font_name="Custom",
                    font_name="Traffolight.otf"
                )
                paragraph.bind(width=lambda inst, val: setattr(inst, "text_size", (val, None)))

                cont_layout.add_widget(heading_title)
                cont_layout.add_widget(paragraph)
                video = Video(
                    source=fav_media,
                    state="play",
                    volume=0,
                    size_hint_y=None,
                    height=dp(150),
                    size_hint_x=0.95,
                    pos_hint={"center_y": .25, "center_x": .5}
                )
                cont_layout.add_widget(video)

                content_card = MDCard(
                    cont_layout,
                    size_hint_y=None,
                    height=dp(300),
                    padding=dp(20),
                    radius=[18, 18, 18, 18],
                    style="outlined",
                    theme_bg_color="Custom",
                    md_bg_color=[0, 1, 1, .2],
                    on_release=lambda instance, topic_title=fav_heading, topic_desc=fav_illustration,
                                      topic_media=fav_media: self.view_fav_content(topic_title, topic_desc, topic_media)
                )

                space = Widget(size_hint_y=None, height=dp(20))
                self.fav_grid.add_widget(content_card)
                self.fav_grid.add_widget(space)

    def view_fav_content(self, topic_title, topic_desc, topic_media, *args):
        self.root.ids.sm.current = "fav_topic_screen"
        media_container = MDRelativeLayout(
            size_hint_y=None,
            height=dp(180)
        )
        grid = self.root.ids.fav_topic_content
        grid.size_hint_y = None
        grid.bind(minimum_height = grid.setter("height"))
        grid.clear_widgets()
        title = topic_title.upper()
        article_text = topic_desc
        media = topic_media

        topic_header = MDLabel(
            text = title,
            halign = "left",
            size_hint_y = None,
            valign = "top",
            adaptive_height = True,
            bold = True,
            theme_font_size = "Custom",
            font_size = sp(18),
            theme_font_name = "Custom",
            font_name = "heading_font.ttf",
            theme_text_color = "Custom",
            text_color = "yellow"
        )
        topic_header.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        article = MDLabel(
            text = article_text,
            size_hint_y = None,
            valign = "top",
            halign = "left",
            theme_text_color = "Custom",
            text_color = [1, 1, 1, 1],
            theme_font_name = "Custom",
            font_name = "times new roman.ttf",
            adaptive_height = True
        )
        article.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        video = Video(
            source=media,
            state="play",
            volume=0,
            size_hint_y=None,
            height=dp(150),
            size_hint_x=None,
            width=dp(300),
            pos_hint={"center_y": .5, "center_x": .5}
        )
        media_container.add_widget(
            video
        )
        open_video_button = MDIconButton(
            icon="open-in-new",
            pos_hint={"center_x": .5, "center_y": .5},
            theme_icon_color="Custom",
            icon_color="magenta",
            theme_bg_color="Custom",
            md_bg_color="white",
            on_release=lambda btn: self.video_view(media)
        )
        media_container.add_widget(open_video_button)
        grid.add_widget(topic_header)
        grid.add_widget(article)
        grid.add_widget(media_container)
    def favorites_screen(self):
        self.root.ids.nav_drawer.set_state("close")
        if self.signedin:
            self.show_favorites()
        else:
            self.open_login_dialog()
    def account_screen(self):
        self.root.ids.nav_drawer.set_state("close")
        if self.signedin:
            self.go_to_account()
        else:
            self.open_login_dialog()
    def explore_content(self):
        self.add_content()
        self.root.ids.nav_drawer.set_state("close")
        self.root.ids.sm.current = "home"
    def view_about(self):
        self.root.ids.nav_drawer.set_state("close")
        self.root.ids.sm.current = "about_screen"

    def go_to_favorites(self):
        self.root.ids.interest_uname.text = self.username
        self.root.ids.sm.current = "interests_screen"
        interests = ["Politics", "Programming", "Art and Craft", "Music and Songs",
                    "Movies and Films", "Lifestyle", "Gossip", "Health and Hygiene",
                    "Space Exploration", "Nature and Wildlife", "Sports"]
        grid = self.root.ids.interests_container
        grid.size_hint_y = None
        grid.bind(minimum_height = grid.setter("height"))
        grid.clear_widgets()
        for interest in interests:
            list_box = MDBoxLayout(
                MDCheckbox(
                    size_hint = (None, None),
                    size = (dp(48), dp(48))
                ),
                MDLabel(
                    text = f"\n{interest}",
                    size_hint_y = None,
                    height = dp(40),
                    valign =  "center"
                ),
                size_hint_y = None,
                height = dp(40),
                spacing = dp(10)
            )
            grid.add_widget(list_box)

    def open_website(self, url):
        webbrowser.open(url)

    def logout(self):
        MDApp.get_running_app().stop()
    


if __name__ == "__main__":
    app = iTREND()
    app.run()