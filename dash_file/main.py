import dash
from dash import html
from dash import dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import sqlite3
import plotly.express as px

# 引入資料庫資料
conn = sqlite3.connect("../pokemon_database.db")
df = pd.read_sql_query("SELECT img_num,name,sp,expertise,level,help_fruit,help_ingredient_1,help_ingredient_num_1,help_ingredient_num_2,help_ingredient_num_3,help_time,help_max,skill_main,power_up,power_down FROM pokemon", conn)
df.loc[0].to_list()

# 表格
columns=[
    {'name':'編號','id':'img_num'},
    {'name':'名稱','id':'name'},
    {'name':'SP值','id':'sp'},
    {'name':'專長','id':'expertise'},
    {'name':'等級','id':'level'},
    {'name':'樹果','id':'help_fruit'},
    {'name':'食材','id':'help_ingredient_1'},
    {'name':'加成1','id':'help_ingredient_num_1'},
    {'name':'加成2','id':'help_ingredient_num_2'},
    {'name':'加成3','id':'help_ingredient_num_3'},
    {'name':'幫忙時間','id':'help_time'},
    {'name':'持有上限','id':'help_max'},
    {'name':'主技能','id':'skill_main'},
    {'name':'性格↑','id':'power_up'},
    {'name':'性格↓','id':'power_down'},
]
table=dash_table.DataTable(
    id='table',
    columns=columns,
    data=df.to_dict("records"),
    page_size=5,
    row_selectable='single',
    filter_action='native',
    style_cell={
        'textAlign':'center',
        'background-color': 'rgba(255, 255, 255, 0.3)',
    }
)

# 整體
app = dash.Dash()
app.layout = html.Div([
    html.Div(id="target",  className="shadow"),
    dbc.Container([table],style={'margin':'0 20px'}, className="shadow mt-5")
], style={'background-image': 'linear-gradient(135deg, #a372c1 0%, #eda1c4 100%)'})

# 圖片 & 圈圈
def JumboItem(name,tags,abls,img):
    hex_area={
        'r':abls,
        'theta':["level",
                  "help_max","help_ingredient_num_1","help_ingredient_num_2","help_ingredient_num_3"],
    }
    fig=px.line_polar(
        hex_area,
        r="r",
        theta="theta",
        line_close=True,
        range_r=[0,40],
        markers='.',
        start_angle=0,
        width=400,
        height=400,
    )
    fig.update_traces(fill="toself")
    fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0)')
    return dbc.Row([
        dbc.Col(
            [
                html.Img(src=img,
                         height='300px',
                         width='300px',
                         ),
                html.H1(name.upper()),
                html.Span([dbc.Badge(i,color='primary',className='mr-1') for i in tags],)
            ],
            width=6,
            align='center',
        ),
        dbc.Col(
            [
                dcc.Graph(figure=fig)
            ],
            width=6,
            style={'marginTop':'100px'}
        )
    ],style={'display':'flex',
             'justify-content': 'space-around','align-items':'center',
             'textAlign':'center',
             'marginBottom':'50px',
             'background-color': 'rgba(0, 0, 0, 0)'}
    )

@app.callback(
    Output("target", "children"), 
    [Input("table", "selected_rows")]
)
def rule(selected_rows):
    if selected_rows:
        pokemon_data = df.iloc[selected_rows[0]]
        name = pokemon_data["name"]
        tags = pokemon_data[["expertise", "help_fruit", "skill_main"]].tolist()
        abls = pokemon_data[["level", "help_max", "help_ingredient_num_1", "help_ingredient_num_2", "help_ingredient_num_3"]].tolist() 
        img_path = f"./assets/img/display/{pokemon_data['img_num']}.png"
        return JumboItem(name, tags, abls, img_path)      
    else:
        return JumboItem("", [], ["level", "help_max", "help_ingredient_num_1", "help_ingredient_num_2", "help_ingredient_num_3"], "")


app.run_server(debug=True)