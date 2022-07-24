from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget




class MainApp(MDApp):
    def on_start(self):
        #set colors
        self.theme_cls.primary_palette = 'Green'

        #add messages
        self.new_message("Jabri Abdessamad", "fashoo fashoo", "1.png")
        self.new_message("jack harlow", "Waspoppin", "2.png")
        self.new_message("dababy", "lesgoooooooo", "1.png")
        self.new_message("pop smoke", "wooooooo", "2.png")
        self.new_message("lil wayne ", "Waspoppin", "1.png")
        self.new_message("tory", "Waspoppin", "2.png")
        self.new_message("travis", "staight uuuuuup", "1.png")
        self.new_message("rich the kid", "Waspoppin", "2.png")
        self.new_message("MB1", "Waspoppin", "1.png")
        self.new_message("D12", "Waspoppin", "2.png")
        self.new_message("Jabri Abdessamad", "fashoo fashoo", "1.png")
        self.new_message("jack harlow", "Waspoppin", "2.png")
        self.new_message("dababy", "lesgoooooooo", "1.png")
        self.new_message("pop smoke", "wooooooo", "2.png")
        self.new_message("lil wayne ", "Waspoppin", "1.png")
        self.new_message("tory", "Waspoppin", "2.png")
        self.new_message("travis", "staight uuuuuup", "1.png")
        self.new_message("rich the kid", "Waspoppin", "2.png")
        self.new_message("MB1", "Waspoppin", "1.png")
        self.new_message("D12", "Waspoppin", "2.png")

    def new_message(self , name , message , image_name):
        new_message = TwoLineAvatarIconListItem(text = name , secondary_text = message )
        new_message.add_widget(ImageLeftWidget(source = image_name))
        self.root.ids.list.add_widget(new_message)

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = ''

class Tab(FloatLayout , MDTabsBase):
    pass



MainApp().run()
