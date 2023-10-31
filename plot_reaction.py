
import openmc
import plotly.graph_objects as go

MT_reaction = 16  # (n,2n)
isotope = 'Be9'

fendl32 = openmc.data.IncidentNeutron.from_hdf5(f'fendl-3.2-hdf5/neutron/{isotope}.h5')
fendl31d = openmc.data.IncidentNeutron.from_hdf5(f'fendl-3.1d-hdf5/neutron/{isotope}.h5')
fendl31a = openmc.data.IncidentNeutron.from_hdf5(f'fendl-3.1a-hdf5/neutron/{isotope}.h5')
fendl30 = openmc.data.IncidentNeutron.from_hdf5(f'fendl-3.0-hdf5/neutron/{isotope}.h5')
fendl21 = openmc.data.IncidentNeutron.from_hdf5(f'fendl-2.1-hdf5/neutron/{isotope}.h5')
endfb71 = openmc.data.IncidentNeutron.from_hdf5(f'endf-b7.1-hdf5/endfb-vii.1-hdf5/neutron/{isotope}.h5')
endfb80 = openmc.data.IncidentNeutron.from_hdf5(f'endf-b8.0-hdf5/endfb-viii.0-hdf5/neutron/{isotope}.h5')
jeff32 = openmc.data.IncidentNeutron.from_hdf5(f'jeff-3.2-hdf5/{isotope}.h5')
jeff33 = openmc.data.IncidentNeutron.from_hdf5(f'jeff-3.3-hdf5/{isotope}.h5')
tendl2019 = openmc.data.IncidentNeutron.from_hdf5(f'tendl-2019-hdf5/tendl-2019-hdf5/{isotope}.h5')
tendl2021 = openmc.data.IncidentNeutron.from_hdf5(f'tendl-2021-hdf5/tendl-2021-hdf5/{isotope}.h5')


fendl32_data = fendl32.reactions[MT_reaction].xs['294K']
fendl31d_data = fendl31d.reactions[MT_reaction].xs['300K']
fendl31a_data = fendl31a.reactions[MT_reaction].xs['300K']
fendl30_data = fendl30.reactions[MT_reaction].xs['300K']
fendl21_data = fendl21.reactions[MT_reaction].xs['300K']
endfb71_data = endfb71.reactions[MT_reaction].xs['294K']
endfb80_data = endfb80.reactions[MT_reaction].xs['294K']
jeff32_data = jeff32.reactions[MT_reaction].xs['294K']
jeff33_data = jeff33.reactions[MT_reaction].xs['294K']
tendl2019_data = tendl2019.reactions[MT_reaction].xs['294K']
tendl2021_data = tendl2021.reactions[MT_reaction].xs['294K']


fig = go.Figure()

fig.add_trace(go.Scatter(x=fendl32_data.x, y=fendl32_data.y, name='FENDL 3.2', line={'dash':'dashdot'}))
fig.add_trace(go.Scatter(x=fendl31d_data.x, y=fendl31d_data.y, name='FENDL 3.1d', line={'dash':'dashdot'}))
fig.add_trace(go.Scatter(x=fendl31a_data.x, y=fendl31a_data.y, name='FENDL 3.1a', line={'dash':'dashdot'}))
fig.add_trace(go.Scatter(x=fendl30_data.x, y=fendl30_data.y, name='FENDL 3.0', line={'dash':'dashdot'}))
fig.add_trace(go.Scatter(x=fendl21_data.x, y=fendl21_data.y, name='FENDL 2.1', line={'dash':'dashdot'}))
fig.add_trace(go.Scatter(x=endfb71_data.x, y=endfb71_data.y, name='ENDF b7.1', line={'dash':'dash'}))
fig.add_trace(go.Scatter(x=endfb80_data.x, y=endfb80_data.y, name='ENDF b8.0', line={'dash':'dash'}))
fig.add_trace(go.Scatter(x=jeff32_data.x, y=jeff32_data.y, name='JEFF 3.2', line={'dash':'dot'}))
fig.add_trace(go.Scatter(x=jeff33_data.x, y=jeff33_data.y, name='JEFF 3.3', line={'dash':'dot'}))
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
