compostos = [{'hidrocarboneto': 'butadieno'}, {'hidrocarboneto': '2,2,3-trimetilpentano'},
             {'hidrocarboneto': '3-metil-4-etil-heptano'},{'hidrocarboneto':'3-metil-ciclobutanol'},
             {'hidrocarboneto': '3-terc-butil-4,5,5-trimetil-2-hepteno'}, {'hidrocarboneto':'ciclopropano'},
             {'hidrocarboneto': 'orto-isopropilfenol'}, {'alcool':'butanodiol'},
             {'alcool': '4-etil-2,5-dimetil-3-heptanol'}, {'alcool':'etanol'}, {'fenol': 'hidroxi-2-metilbenzeno'},
             {'fenol': 'hidroxi-3-metilbenzeno'}, {'fenol': "hidroxi-4-metilbenzeno"}, {'fenol': 'hidroxibenzeno'},
             {'cetona': '2-pentanona'}, {'cetona': 'pentanona'}, {'cetona': '4-etil-4-penten-2-ona'},
             {'cetona': 'butanona'}, {'cetona': 'propanona'}, {'amida': '3,3,4-trimetil-hexanamida'},
             {'amida': '3-etil-3,4,4,5-tetrametil-hexanamida'}, {'amida': 'isopropiloctanamida'},
             {'ésteres': 'fenilbutanoato de isopropila'}, {'enol': '3-metil-3-buten-1-ol'},
             {'aldeidos': '3-metil-3-pentenal'}, {'amina': '4-metil-heptan-2-amina'},
             {'ester': '4-metilpentanoato de metila'}, {'acido carboxilico': 'acido 2-etil-4-metiloctanoico'},
             {'acido carboxilico': 'acido 3-metilpentanoico'}, {'acido carboxilico': 'butanodioico'},
             {'acido carboxilico': 'acido etanoico'}, {'acido carboxilico': 'acido propanoico'},
             {'amina': 'butan-2-3-diamina'}, {'aldeido': 'butanal'}, {'amida': 'butanamida'},
             {'anina': 'butiletilmetilamina'}, {'aldeido': 'etanal'}, {'amida': 'etanamida'},
             {'ester': 'etanoato de pentila'}, {'ester': 'etanoato de terc-butila'}, {'amina': 'etilmetilamina'},
             {'ester': 'etoxi-etano'}, {'ester': 'etoxi-propano'}, {'aldeído': 'metanal'},
             {'ester': 'metanoato de isobutila'}, {'ester': 'metoxi--etano'}, {'ester': 'metoxi-isopropano'},
             {'aldeído': 'propanal'}, {'ester': 'propoxi-propano'}, {'amina': 'trimetilamina'}]
nome = str(input('digite no nome do composto: ')).strip().lower()
for e in compostos:
    for k, v in e.items():
        if v == nome:
            print(f'\npertence a função organica:  {k}')