from bokeh.plotting import figure, output_notebook,show
 
pacers_blue = "#00FF04"
pacers_gold = "#FFC633"
pacers_silver = "#BEC0C2"
pacers_white = "#f0ff00"
pacers_court = "#EBB889"
pacers_court_2 = "#F2D3B8"
pacers_text = "Houston Rockets"
 
output_notebook()
 
court = figure(plot_width=700, plot_height=700)
 
# Outside court dimensions: 636 x 600
court.quad(top=600, bottom=0, right=636, left=-36, alpha=0.5, line_width=2, color=pacers_court_2)
# Court dimensions: 600in x 564in
court.quad(top=564, bottom=0, right=600, left=0, alpha=0.5, line_width=2, color=pacers_court)
# Pacers text:
court.text(300,564, text=[pacers_text], text_alpha=1, text_color=pacers_blue, text_align="center", text_font='helvetica', text_font_style="bold")
# NBA lane dimensions: 192in wide, 228in tall
court.quad(top=564, bottom=372, right=396, left=204, alpha=1, line_width=2, color=pacers_blue)
# NCAA lane dimensions: 144in wide, 228in tall
court.quad(top=564, bottom=372, right=372, left=228, alpha=1, color=pacers_blue, line_alpha=1, line_width=2, line_color=pacers_white)
# Hoop dimensions: radius of 9in; Hoop reference: 300in, 507in
court.annulus(300,507, inner_radius=9, outer_radius=9, color="orange", alpha=0.9)
# Backboard dimensions: thickness is negligible, width is 72in ; Backboard reference: 264, 516
court.line([264, 336], [516, 516], line_width=2, line_color="orange", line_alpha=0.9)
# Free throw arcs dimensions: radius is 72in; Free throw arc reference: 300, 372
court.arc(300,372,radius=72, start_angle=180, start_angle_units='deg', end_angle=360, end_angle_units='deg', line_width=2, line_color=pacers_white)
court.arc(300,372,radius=72, start_angle=0, start_angle_units='deg', end_angle=360, end_angle_units='deg', line_width=2, line_color=pacers_white, line_dash=[2,1])
# Three point line arc dimensions: radius is 285 inches; Three point line arc reference: 300,507
court.arc(300,507,radius=285, start_angle=202.5, start_angle_units='deg', end_angle=337.5, end_angle_units='deg', line_width=2, line_color=pacers_white)
# Three point line corner dimensions: length is 168in; Corner reference: 36 & 564
court.line([36,36],[396,564], line_width=2, line_color=pacers_white)
court.line([564,564],[396,564], line_width=2, line_color=pacers_white)
# Block dimensions: bigblock is a 12x8 rectangle, others are lines; Block reference: 84in, 132in, 168in
## Big blocks
court.quad(top=480, bottom=468, right=204, left=196, alpha=1, color=pacers_white)
court.quad(top=480, bottom=468, right=404, left=396, alpha=1, color=pacers_white)
## Smaller blocks
court.line([196,204],[432,432])
court.line([196,204], [396,396])
court.line([396,404], [432,432])
court.line([396,404], [396, 396])

#p = figure(title = "simple line example", plot_height = 700, plot_width = 600)
court.scatter(shot_df.LOC_X, shot_df.LOC_Y)

show(p)
show(court)
