import dash
from dash import dcc, html, dash_table
import sqlite3

app = dash.Dash(__name__)

# Create a list of dictionaries for DataTable columns
column_names = ['Player', 'Price', 'Type', 'I / F']
datatable_columns = [{'name': col, 'id': col} for col in column_names]

# Define layout
app.layout = html.Div(style={'backgroundColor': 'black', 'color': 'white'}, children=[
    html.H1("ETC IPL Auction 2025", style={'text-align': 'center'}),

    html.Div([
        dcc.Dropdown(
            id='player',
            options=[],
            placeholder = 'Choose Player',
            style={'width': '100%','color': 'black','text-align': 'center'}  # Make the dropdown span across the entire row
        ),
        dcc.Dropdown(
            id='team',
            options=[
                {'label': 'RCB', 'value': 'RCB'},
                {'label': 'SRH', 'value': 'SRH'},
                {'label': 'CSK', 'value': 'CSK'},
                {'label': 'KKR', 'value': 'KKR'},
                {'label': 'MI', 'value': 'MI'},
                {'label': 'GT', 'value': 'GT'},
                {'label': 'RR', 'value': 'RR'},
                {'label': 'LSG', 'value': 'LSG'},
                {'label': 'DC', 'value': 'DC'},
                {'label': 'PBKS', 'value': 'PBKS'}
            ],
            placeholder = 'Choose Team',
            style={'width': '100%','color': 'black','text-align': 'center'}  # Make the dropdown span across the entire row
        ),
        dcc.Dropdown(
            id='price',
            options=[
                {'label': '20 L', 'value': 20},
                {'label': '30 L', 'value': 30},
                {'label': '40 L', 'value': 40},
                {'label': '50 L', 'value': 50},
                {'label': '60 L', 'value': 60},
                {'label': '70 L', 'value': 70},
                {'label': '80 L', 'value': 80},
                {'label': '90 L', 'value': 90},
                {'label': '1 Cr', 'value': 100},
                {'label': '1.25 Cr', 'value': 125},
                {'label': '1.50 Cr', 'value': 150},
                {'label': '1.75 Cr', 'value': 175},
                {'label': '2 Cr', 'value': 200},
                {'label': '2.25 Cr', 'value': 225},
                {'label': '2.50 Cr', 'value': 250},
                {'label': '2.75 Cr', 'value': 275},
                {'label': '3 Cr', 'value': 300},
                {'label': '3.25 Cr', 'value': 325},
                {'label': '3.50 Cr', 'value': 350},
                {'label': '3.75 Cr', 'value': 375},
                {'label': '4 Cr', 'value': 400},
                {'label': '4.25 Cr', 'value': 425},
                {'label': '4.50 Cr', 'value': 450},
                {'label': '4.75 Cr', 'value': 475},
                {'label': '5 Cr', 'value': 500},
                {'label': '5.5 Cr', 'value': 550},
                {'label': '6 Cr', 'value': 600},
                {'label': '6.5 Cr', 'value': 650},
                {'label': '7 Cr', 'value': 700},
                {'label': '7.5 Cr', 'value': 750},
                {'label': '8 Cr', 'value': 800},
                {'label': '8.5 Cr', 'value': 850},
                {'label': '9 Cr', 'value': 900},
                {'label': '9.5 Cr', 'value': 950},
                {'label': '10 Cr', 'value': 1000},
                {'label': '10.5 Cr', 'value': 1050},
                {'label': '11 Cr', 'value': 1100},
                {'label': '11.5 Cr', 'value': 1150},
                {'label': '12 Cr', 'value': 1200},
                {'label': '12.5 Cr', 'value': 1250},
                {'label': '13 Cr', 'value': 1300},
                {'label': '13.5 Cr', 'value': 1350},
                {'label': '14 Cr', 'value': 1400},
                {'label': '14.5 Cr', 'value': 1450},
                {'label': '15 Cr', 'value': 1500},
                {'label': '15.5 Cr', 'value': 1550},
                {'label': '16 Cr', 'value': 1600},
                {'label': '16.5 Cr', 'value': 1650},
                {'label': '17 Cr', 'value': 1700},
                {'label': '17.5 Cr', 'value': 1750},
                {'label': '18 Cr', 'value': 1800},
                {'label': '18.5 Cr', 'value': 1850},
                {'label': '19 Cr', 'value': 1900},
                {'label': '19.5 Cr', 'value': 1950},
                {'label': '20 Cr', 'value': 2000},
                {'label': '20.5 Cr', 'value': 2050},
                {'label': '21 Cr', 'value': 2100},
                {'label': '21.5 Cr', 'value': 2150},
                {'label': '22 Cr', 'value': 2200},
                {'label': '22.5 Cr', 'value': 2250},
                {'label': '23 Cr', 'value': 2300},
                {'label': '23.5 Cr', 'value': 2350},
                {'label': '24 Cr', 'value': 2400},
                {'label': '24.5 Cr', 'value': 2450},
                {'label': '25 Cr', 'value': 2500},
                {'label': 'Retain', 'value': 0}
            ],
            placeholder = 'Choose Price',
            style={'width': '100%','color': 'black','text-align': 'center'}  # Make the dropdown span across the entire row
        ),
        html.Button('SELL Player', id='sell', n_clicks=0, style={'width': '70%'}),
        html.Button('UNDO', id='undo', n_clicks=0, style={'width': '70%'}),
    ], style={'display': 'flex'}),

    html.Div([
        html.Div([
            html.H2('RCB', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table1',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': '#ff0000',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team1',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

        html.Div([], style={'width': '1%', 'display': 'inline-block'}),
        
        html.Div([
            html.H2('SRH', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table2',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': 'orange',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team2',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

        html.Div([], style={'width': '1%', 'display': 'inline-block'}),

        html.Div([
            html.H2('CSK', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table3',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': '#FFFF00',
                            'color': 'black',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team3',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

        html.Div([], style={'width': '1%', 'display': 'inline-block'}),

        html.Div([
            html.H2('KKR', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table4',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': 'purple',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team4',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

        html.Div([], style={'width': '1%', 'display': 'inline-block'}),

        html.Div([
            html.H2('DC', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table9',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': 'blue',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team9',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

    ], style={'display': 'flex'}),

    html.Div([
        html.Div([
            html.H2('MI', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table5',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': 'blue',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team5',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

        html.Div([], style={'width': '1%', 'display': 'inline-block'}),

        html.Div([
            html.H2('GT', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table6',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': '#A9A9A9',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team6',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

        html.Div([], style={'width': '1%', 'display': 'inline-block'}),

        html.Div([
            html.H2('RR', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table7',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': '#B33B72',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team7',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

        html.Div([], style={'width': '1%', 'display': 'inline-block'}),

        html.Div([
            html.H2('LSG', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table8',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': '#ADD8E6',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team8',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),

        html.Div([], style={'width': '1%', 'display': 'inline-block'}),

        html.Div([
            html.H2('PBKS', style={'text-align': 'center'}),
            dash_table.DataTable(
                id='table10',
                columns=datatable_columns,
                data=[],
                style_table={'margin': 'auto'},
                style_data={'backgroundColor': 'red',
                            'color': 'white',},
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'blue',
                },
                style_cell={'textAlign': 'center'},
            ),
            html.Div(id='team10',style={'white-space': 'pre-line', 'text-align': 'center','background-color': '#f0f0f0',  # Light gray background color
                    'color': 'blue'})
        ], style={'width': '20%', 'display': 'inline-block'}),
    ], style={'display': 'flex'}),
    
])

# Store previous click counts
previous_clicks = {'sell': 0, 'undo': 0}

# Define callback to update output
@app.callback(
    [dash.dependencies.Output('player', 'options'),
     dash.dependencies.Output('team', 'value'),
     dash.dependencies.Output('price', 'value'),
     dash.dependencies.Output('table1', 'data'),
     dash.dependencies.Output('team1', 'children'),
     dash.dependencies.Output('table2', 'data'),
     dash.dependencies.Output('team2', 'children'),
     dash.dependencies.Output('table3', 'data'),
     dash.dependencies.Output('team3', 'children'),
     dash.dependencies.Output('table4', 'data'),
     dash.dependencies.Output('team4', 'children'),
     dash.dependencies.Output('table5', 'data'),
     dash.dependencies.Output('team5', 'children'),
     dash.dependencies.Output('table6', 'data'),
     dash.dependencies.Output('team6', 'children'),
     dash.dependencies.Output('table7', 'data'),
     dash.dependencies.Output('team7', 'children'),
     dash.dependencies.Output('table8', 'data'),
     dash.dependencies.Output('team8', 'children'),
     dash.dependencies.Output('table9', 'data'),
     dash.dependencies.Output('team9', 'children'),
     dash.dependencies.Output('table10', 'data'),
     dash.dependencies.Output('team10', 'children')],
    [dash.dependencies.Input('sell', 'n_clicks'),
     dash.dependencies.Input('undo', 'n_clicks')],
    [dash.dependencies.State('player', 'value'),
     dash.dependencies.State('team', 'value'),
     dash.dependencies.State('price', 'value')]
)
def update_output(button1_clicks, button2_clicks, player, team, price):
    global previous_clicks
    
    conn = sqlite3.connect('ipl.db')
    cur = conn.cursor()

    return_list = []

    # Determine if each button was clicked since last callback invocation
    sell_pressed = button1_clicks > previous_clicks['sell']
    undo_pressed = button2_clicks > previous_clicks['undo']

    # Update previous click counts
    previous_clicks['sell'] = button1_clicks
    previous_clicks['undo'] = button2_clicks

    if undo_pressed:
        cur.execute("DELETE FROM buys WHERE timestamp = (SELECT MAX(timestamp) FROM buys)")
        conn.commit()
        print("Last inserted record deleted successfully.")
    
    if sell_pressed:
        print(player, team, price)
        print(type(player), type(team), type(price))
        if player is not None and team is not None and price is not None:
            cur.execute('SELECT id from players where name = ?', (player,))
            player_id = cur.fetchone()[0]
            cur.execute('INSERT INTO buys(player_id, price, team) VALUES (?,?,?)',(player_id, price, team))
            conn.commit()
            print("player sold")
    
    # subquery to have only players that are still unsold
    cur.execute("SELECT name, name FROM players where id not in (select player_id from buys)")
    options_from_db = cur.fetchall()

    options = [{'label': label, 'value': value} for label, value in options_from_db]
    return_list.append(options)
    return_list.append(None) # reset team and price dropdown 
    return_list.append(None)

    team_list = ['RCB','SRH','CSK','KKR','MI','GT','RR','LSG','DC','PBKS']

    for team_name in team_list:
        cur.execute('SELECT p.name,b.price,p.type,SUBSTR(p.country, 1, 1) AS country_initial FROM players AS p INNER JOIN buys AS b ON p.id = b.player_id WHERE b.team = ?;',(team_name,))
        data = cur.fetchall()
        print(team_name, '-----------------')
        print(data)
        formatted_data = [dict(zip(['Player', 'Price','Type','I / F'], row)) for row in data]
        print(formatted_data)
        return_list.append(formatted_data)

        cur.execute('SELECT sum(b.price) FROM players AS p INNER JOIN buys AS b ON p.id = b.player_id WHERE b.team = ?;',(team_name,))
        purse_used = cur.fetchone()[0]
        if purse_used is None:
            purse_used = 0
        purse_rem  = 5000 - purse_used

        cur.execute('SELECT count(p.country) FROM players AS p INNER JOIN buys AS b ON p.id = b.player_id WHERE b.team = ? AND p.country="Indian";',(team_name,))
        indians = cur.fetchone()[0]
        cur.execute('SELECT count(p.country) FROM players AS p INNER JOIN buys AS b ON p.id = b.player_id WHERE b.team = ? AND p.country="Foreigner";',(team_name,))
        foreigners = cur.fetchone()[0]

        cur.execute('SELECT count(p.type) FROM players AS p INNER JOIN buys AS b ON p.id = b.player_id WHERE b.team = ? AND p.type="Bowler";',(team_name,))
        bowlers = cur.fetchone()[0]
        cur.execute('SELECT count(p.type) FROM players AS p INNER JOIN buys AS b ON p.id = b.player_id WHERE b.team = ? AND p.type="Batsman";',(team_name,))
        batsman = cur.fetchone()[0]
        cur.execute('SELECT count(p.type) FROM players AS p INNER JOIN buys AS b ON p.id = b.player_id WHERE b.team = ? AND p.type="All Rounder";',(team_name,))
        all_round = cur.fetchone()[0]
        cur.execute('SELECT count(p.type) FROM players AS p INNER JOIN buys AS b ON p.id = b.player_id WHERE b.team = ? AND p.type="Wicket Keeper";',(team_name,))
        wk = cur.fetchone()[0]

        print(purse_used,purse_rem,indians,foreigners,bowlers,batsman,all_round,wk)
        info = '\nPurse Used : ' + str(purse_used) + ' Lakhs\n'
        info += 'Purse Available : ' + str(purse_rem) + ' Lakhs\n\n'

        info += "Indians : " + str(indians) + '\nForeigners : ' + str(foreigners) + '\n'
        info += "    Batsman   (min 2) : " + str(batsman) + '\n'
        info += " All Rounders (min 2) : " + str(all_round) + '\n'
        info += "    Bowlers   (min 3) : " + str(bowlers) + '\n'
        info += "      WK      (min 1) : " + str(wk) + '\n\n'
        return_list.append(info)
    conn.close()
    return return_list
if __name__ == '__main__':
    app.run_server(debug=True)
