import plotly.express as px

#cores discretas qualitativas
color_discrete_G10 = px.colors.qualitative.G10
color_discrete_Pastel = px.colors.qualitative.Pastel
color_discrete_Antique = px.colors.qualitative.Antique

#cores escalares
color_scale_cividis = 'Cividis'
color_cividis = ['#004080', '#0059b3', '#666699', '#8585ad', '#b8b894', '#ffff00']

#função para apresentar os tipos de cores qualitativas
def show_qualitative_colors():
    colors = px.colors.qualitative.swatches()
    colors.show()