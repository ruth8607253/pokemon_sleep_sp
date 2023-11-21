def load_treeview(self):
        selected_option = self.data_var.get()
        selected_year = self.year_var.get()
        selected_month = self.month_var.get()
        selected_area = self.area_var.get()
        selected_industry = self.industry_var.get()

        if selected_option and selected_year:
            sql = f"SELECT * FROM {selected_option} WHERE 年 = '{selected_year}'"

            if selected_month and selected_month != "Select Month":
                sql += f" AND 月 = '{selected_month}'"
            
            if selected_area and selected_area != "Select Area":
                sql += f" AND 地區 = '{selected_area}'"

            if selected_industry and selected_industry != "Select Industry":
                sql += f" AND 產業別 = '{selected_industry}'"

            data = pd.read_sql_query(sql, self.conn)
            self.display_data(data)

    def display_data(self, data):
        self.treeview.delete(*self.treeview.get_children())  # 清空 Treeview

        if not data.empty:
            columns = list(data.columns)
            self.treeview["columns"] = columns
            for col in columns:
                self.treeview.heading(col, text=col, anchor="w")
                self.treeview.column(col, anchor="w", width=100)  # 設定欄位寬度，可以自行調整

            for index, row in data.iterrows():
                values = [row[col] for col in columns]
                self.treeview.insert("", "end", values=values)