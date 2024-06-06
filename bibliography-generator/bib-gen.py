#!/usr/bin/python
import yaml
import os

def get_pages_num(section, article):
    sec = os.path.join("./", section)
    tex_for_page_parse = "_section-overlay.tex"
    tex_file = os.path.join(sec, tex_for_page_parse)

    with open(tex_file, 'r') as f:
        contents = f.readlines()
    target = []
    c_iter = iter(contents)
    while True:
        line = next(c_iter, "end")
        if article in line:
            while True:
                if line.strip():
                    if "newpage" in line:
                        line = next(c_iter, "end")
                        continue
                    elif "renewcommand" in line:
                        break
                    elif "end" in line:
                        break
                    else:
                        target.append(line.strip())
                        line = next(c_iter, "end")
                        continue
                else:
                    line = next(c_iter, "end")
            break
        elif line == "end":
            break
    strf = target[0]
    ind_f = strf.find("{abspage-")
    sliced_f = strf[ind_f+9:]
    first_page = ""
    last_page = ""
    for c in sliced_f:
        if c.isdigit():
            first_page += c
        else:
            break
    strl = target[-1]
    ind_l = strl.find("\\rhead{~~")
    if ind_l == -1:
        ind_l = strl.find("\\lhead{")
        sliced_l = strl[ind_l+7:]
    else:
        sliced_l = strl[ind_l+9:]
    for c in sliced_l:
        if c.isdigit():
            last_page += c
        else:
            break
    return [first_page, last_page]

directory = '.'
bib = open("./spisok.bib", 'w', 2, 'utf-8')

m_file = open("../bibliography-generator/meta.yaml", 'r')
meta = yaml.load(m_file, Loader=yaml.FullLoader)

for sec_folder in os.listdir(directory):
    dirname = os.path.join(directory, sec_folder)
    if os.path.isdir(dirname):
        sec_yaml_file = open(os.path.join(dirname, "section.yml",), 'r')
        data = yaml.load(sec_yaml_file, Loader=yaml.FullLoader)
        for art in data['articles']:
            [first_page, last_page] = get_pages_num(sec_folder, art['title'])
            bib.write("@inproceedings{Typeclass,\n")
            bib.write("  author = {%s},\n" % (" and ".join(art['by'])))
            bib.write("  title ={%s},\n" % (art['title']))
            bib.write("  booktitle = {%s},\n" % (meta['booktitle']))
            bib.write("  series = {%s},\n" % (meta['series']))
            bib.write("  year = {%s},\n" % (meta['year']))
            bib.write("  issn = {%s},\n" % (meta['issn']))
            bib.write("  location = {%s},\n" % (meta['location']))
            bib.write("  pages = {%s--%s},\n" % (first_page, last_page))
            bib.write("  numpages = {%i},\n" % (int(last_page)-int(first_page)+1))
            bib.write("  publisher = {%s},\n" % (meta['publisher']))
            bib.write("  address = {%s},\n}\n\n" % (meta['address']))
            
