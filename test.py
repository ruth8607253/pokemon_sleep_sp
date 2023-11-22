children = self.get_children()

        for child in children:
            item = self.item(child)
            name = item['values'][0].lower()
            help_fruit = item['values'][3].lower()
            help_ingredient = item['values'][4].lower() if len(item['values']) > 4 else ""

            # 根据条件筛选数据
            if (text in name) or (ingredient in help_ingredient) or (fruit in help_fruit):
                self.item(child, open=True)
            else:
                self.item(child, open=False)

        # 如果搜索文本和果实类型都为空，显示全部数据
        if text == "" and fruit == "樹果類型" and ingredient == "食材類型":
            for child in children:
                self.item(child, open=True)
