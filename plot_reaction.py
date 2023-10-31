
import openmc
import plotly.graph_objects as go

MT_reaction = 205
isotope = 'Li7'

fendl32 = openmc.data.IncidentNeutron.from_hdf5(f'fendl-3.2-hdf5/neutron/{isotope}.h5')
fendl31d = openmc.data.IncidentNeutron.from_hdf5(f'fendl-3.1d-hdf5/neutron/{isotope}.h5')
# fendl31a = openmc.data.IncidentNeutron.from_hdf5(f'fendl-3.1a-hdf5/neutron/{isotope}.h5') TODO fix this
fendl30 = openmc.data.IncidentNeutron.from_hdf5(f'fendl-3.0-hdf5/neutron/{isotope}.h5')
fendl21 = openmc.data.IncidentNeutron.from_hdf5(f'fendl-2.1-hdf5/neutron/{isotope}.h5')
# endfb71 = openmc.data.IncidentNeutron.from_hdf5(f'endf-7.1-ace/')
# endfb80 = openmc.data.IncidentNeutron.from_hdf5(f'endf-8.0-ace/')
jeff32 = openmc.data.IncidentNeutron.from_hdf5(f'jeff-3.2-hdf5/{isotope}.h5')
# jeff33 = openmc.data.IncidentNeutron.from_hdf5(f'jeff-3.3-hdf5/{isotope}.h5')
tendl2019 = openmc.data.IncidentNeutron.from_hdf5(f'tendl-2019-hdf5/tendl-2019-hdf5/{isotope}.h5')
tendl2021 = openmc.data.IncidentNeutron.from_hdf5(f'tendl-2021-hdf5/tendl-2021-hdf5/{isotope}.h5')


fendl32_data = fendl32.reactions[MT_reaction].xs['294K']
fendl31d_data = fendl31d.reactions[MT_reaction].xs['300K']
# fendl31a_data = fendl31a.reactions[MT_reaction]['294K']
fendl30_data = fendl30.reactions[MT_reaction].xs['300K']
fendl21_data = fendl21.reactions[MT_reaction].xs['300K']
# endfb71_data = endfb71.reactions[MT_reaction]['294K']
# endfb80_data = endfb80.reactions[MT_reaction]['294K']
jeff32_data = jeff32.reactions[MT_reaction].xs['294K']
# jeff33_data = jeff33.reactions[MT_reaction].xs['294K']
tendl2019_data = tendl2019.reactions[MT_reaction].xs['294K']
tendl2021_data = tendl2021.reactions[MT_reaction].xs['294K']


fig = go.Figure()

fig.add_trace(go.Scatter(x=fendl32_data.x, y=fendl32_data.y, name='FENDL 3.2'))
fig.add_trace(go.Scatter(x=fendl31d_data.x, y=fendl31d_data.y, name='FENDL 3.1d'))
# fig.add_trace(go.Scatter(x=fendl31a_data.x, y=fendl31a_data.y, name='FENDL 3.1a'))
fig.add_trace(go.Scatter(x=fendl30_data.x, y=fendl30_data.y, name='FENDL 3.0'))
fig.add_trace(go.Scatter(x=fendl21_data.x, y=fendl21_data.y, name='FENDL 2.1'))
# fig.add_trace(go.Scatter(x=endfb71_data.x, y=endfb71_data.y, name='ENDF b7.1'))
# fig.add_trace(go.Scatter(x=endfb80_data.x, y=endfb80_data.y, name='ENDF b8.0'))
fig.add_trace(go.Scatter(x=jeff32_data.x, y=jeff32_data.y, name='JEFF 3.2'))
# fig.add_trace(go.Scatter(x=jeff33_data.x, y=jeff33_data.y, name='JEFF 3.3'))
fig.add_trace(go.Scatter(x=tendl2019_data.x, y=tendl2019_data.y, name='TENDL 2019'))
fig.add_trace(go.Scatter(x=tendl2021_data.x, y=tendl2021_data.y, name='TENDL 2021'))


fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.update_layout(
    title=f"Comparison of MT {MT_reaction} reaction for multiple nuclear data libraries",
    yaxis_title="Cross section [barns]",
    xaxis_title="Energy [eV]")

fig.write_html("index.html")

fig.show()
