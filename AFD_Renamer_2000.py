import os

directory = input(str('Digite o Diretório: '))

files = os.listdir(directory)
txt_files = [f for f in files if f.endswith(".txt")]

for txt_file in txt_files:
    file_name = os.path.splitext(txt_file)[0]
    full_name = file_name
    
    if "2004" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID SANTOS DUMONT " + full_name + ".txt"
    if "2005" in full_name:
        new_file_name = "OPTY BELA VISTA " + full_name + ".txt"
    if "2006" in full_name:
        new_file_name = "BANCO DE SANGUE " + full_name + ".txt"
    if "2009" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID JARDIM IMBUIAS " + full_name + ".txt"
    if "2010" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID ANCHIETA - BENJAMIN CONSTANT " + full_name + ".txt"
    if "2014" in full_name:
        new_file_name = "UHG-SP-AMIL TOWER MORUMBI " + full_name + ".txt"
    if "2015" in full_name:
        new_file_name = "INSIDE-SP-INSIDE DIAGNOSTICOS " + full_name + ".txt"
    if "2016" in full_name:
        new_file_name = "WANA INDUSTRIA-SP-WANA INDUSTRIA " + full_name + ".txt"
    if "2019" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID ARARAQUARA " + full_name + ".txt"
    if "2021" in full_name:
        new_file_name = "UHG-SP-ANA COSTA-P.S GUARUJA " + full_name + ".txt"
    if "2022" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID FRANCA " + full_name + ".txt"
    if "2030" in full_name:
        new_file_name = "UHG-SP-ANA COSTA-P.S SAO VICENTE " + full_name + ".txt"
    if "2031" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID JOAO DIAS " + full_name + ".txt"

    
    os.rename(os.path.join(directory, txt_file), os.path.join(directory, new_file_name))

