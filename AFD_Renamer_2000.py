import os

directory = input(str('Cole o Diretório Desejado: '))

files = os.listdir(directory)
txt_files = [f for f in files if f.endswith(".txt")]
numbers_to_check = ["2004", "2005", "2006", "2009", "2010", "2014", "2015", "2016", "2019", "2021", "2022", "2030", "2031","2023","2013","2020","2002","2001"]
for txt_file in txt_files:
    file_name = os.path.splitext(txt_file)[0]
    full_name = file_name
    
    if "2004" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID SANTOS DUMONT " + full_name + ".txt"
        if "2004" in numbers_to_check:
            numbers_to_check.remove("2004")
            print(numbers_to_check)
    if "2005" in full_name:
        new_file_name = "OPTY BELA VISTA " + full_name + ".txt"
        if "2005" in numbers_to_check:
            numbers_to_check.remove("2005")
            print(numbers_to_check)
    if "2006" in full_name:
        new_file_name = "BANCO DE SANGUE " + full_name + ".txt"
        if "2006" in numbers_to_check:
            numbers_to_check.remove("2006")
            print(numbers_to_check)
    if "2009" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID JARDIM IMBUIAS " + full_name + ".txt"
        if "2009" in numbers_to_check:
            numbers_to_check.remove("2009")
            print(numbers_to_check)
    if "2010" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID ANCHIETA - BENJAMIN CONSTANT " + full_name + ".txt"
        if "2010" in numbers_to_check:
            numbers_to_check.remove("2010")
            print(numbers_to_check)
    if "2014" in full_name:
        new_file_name = "UHG-SP-AMIL TOWER MORUMBI " + full_name + ".txt"
        if "2014" in numbers_to_check:    
            numbers_to_check.remove("2014")
            print(numbers_to_check)
    if "2015" in full_name:
        new_file_name = "INSIDE-SP-INSIDE DIAGNOSTICOS " + full_name + ".txt"
        if "2015" in numbers_to_check:
            numbers_to_check.remove("2015")
            print(numbers_to_check)
    if "2016" in full_name:
        new_file_name = "WANA INDUSTRIA-SP-WANA INDUSTRIA " + full_name + ".txt"
        if "2016" in numbers_to_check:
            numbers_to_check.remove("2016")
            print(numbers_to_check)
    if "2019" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID ARARAQUARA " + full_name + ".txt"
        if "2019" in numbers_to_check:
            numbers_to_check.remove("2019")
            print(numbers_to_check)
    if "2021" in full_name:
        new_file_name = "UHG-SP-ANA COSTA-P.S GUARUJA " + full_name + ".txt"
        if "2021" in numbers_to_check:
            numbers_to_check.remove("2021")
            print(numbers_to_check)
    if "2022" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID FRANCA " + full_name + ".txt"
        if "2022" in numbers_to_check:
            numbers_to_check.remove("2022")
            print(numbers_to_check)
    if "2030" in full_name:
        new_file_name = "UHG-SP-ANA COSTA-P.S SAO VICENTE " + full_name + ".txt"
        if "2030" in numbers_to_check:
            numbers_to_check.remove("2030")
            print(numbers_to_check)
    if "2031" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID JOAO DIAS " + full_name + ".txt"
        if "2031" in numbers_to_check:
            numbers_to_check.remove("2031")
            print(numbers_to_check)
    if "2023" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID SAO JOSE RIO PRETO " + full_name + ".txt"
        if "2023" in numbers_to_check:
            numbers_to_check.remove("2023")
            print(numbers_to_check)
    if "2013" in full_name:
        new_file_name = "FRESENIUS-SP-UNID JARDIM " + full_name + ".txt"
        if "2013" in numbers_to_check:
            numbers_to_check.remove("2013")
            print(numbers_to_check)
    if "2020" in full_name:
        new_file_name = "UHG-SP-NEXT-UNID DIADEMA " + full_name + ".txt"
        if "2020" in numbers_to_check:
            numbers_to_check.remove("2020")
            print(numbers_to_check)
    if "2002" in full_name:
        new_file_name = "DAVITA-SP-NEFRO-UNID SAO CAETANO SUL " + full_name + ".txt"
        if "2002" in numbers_to_check:
            numbers_to_check.remove("2002")
            print(numbers_to_check)
    if "2001" in full_name:
        new_file_name = "FRESENIUS VILA MARIANA	 " + full_name + ".txt"
        if "2001" in numbers_to_check:
            numbers_to_check.remove("2001")
            print(numbers_to_check)
    
    os.rename(os.path.join(directory, txt_file), os.path.join(directory, new_file_name))


if "2004" in numbers_to_check:
            print(f"DAVITA-SP-NEFRO-UNID SANTOS DUMONT Não produziu arquivos AFD")
if "2005" in numbers_to_check:
            print(f"OPTY BELA VISTA Não produziu arquivos AFD")
if "2006" in numbers_to_check:
            print(f"BANCO DE SANGUE Não produziu arquivos AFD")
if "2009" in numbers_to_check:
            print(f"DAVITA-SP-NEFRO-UNID JARDIM IMBUIAS Não produziu arquivos AFD")
if "2010" in numbers_to_check:
            print(f"DAVITA-SP-NEFRO-UNID ANCHIETA - BENJAMIN CONSTANT Não produziu arquivos AFD")
if "2014" in numbers_to_check:
            print(f"UHG-SP-AMIL TOWER MORUMBI Não produziu arquivos AFD")
if "2015" in numbers_to_check:
            print(f"INSIDE-SP-INSIDE DIAGNOSTICOS Não produziu arquivos AFD")
if "2016" in numbers_to_check:
            print(f"WANA INDUSTRIA-SP-WANA INDUSTRIA Não produziu arquivos AFD")
if "2019" in numbers_to_check:
            print(f"DAVITA-SP-NEFRO-UNID ARARAQUARA Não produziu arquivos AFD")
if "2021" in numbers_to_check:
            print(f"UHG-SP-ANA COSTA-P.S GUARUJA Não produziu arquivos AFD")
if "2022" in numbers_to_check:
            print(f"DAVITA-SP-NEFRO-UNID FRANCA Não produziu arquivos AFD")
if "2030" in numbers_to_check:
            print(f"UHG-SP-ANA COSTA-P.S SAO VICENTE Não produziu arquivos AFD")
if "2031" in numbers_to_check:
            print(f"DAVITA-SP-NEFRO-UNID JOAO DIAS Não produziu arquivos AFD")
if "2023" in numbers_to_check:
            print(f"DAVITA-SP-NEFRO-UNID SAO JOSE RIO PRETO Não produziu arquivos AFD")
if "2013" in numbers_to_check:
            print(f"FRESENIUS-SP-UNID JARDIM Não produziu arquivos AFD")
if "2020" in numbers_to_check:
            print(f"UHG-SP-NEXT-UNID DIADEMA Não produziu arquivos AFD")
if "2002" in numbers_to_check:
            print(f"DAVITA-SP-NEFRO-UNID SAO CAETANO SUL Não produziu arquivos AFD")
if "2001" in numbers_to_check:
            print(f"FRESENIUS VILA MARIANA Não produziu arquivos AFD")