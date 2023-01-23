from pypdf import PdfWriter, PdfReader, Transformation
import glob


# EN POSITIVO PARA SUBIR LA TRASERA
#CORRECCION_EN_PIXELES_VERTICAL = 0
#CORRECCION_EN_PIXELES_HORIZONTAL = 0
#ANGULO = 0


def procesar(CORRECCION_EN_PIXELES_VERTICAL ,CORRECCION_EN_PIXELES_HORIZONTAL, ANGULO):

    dir_entrada = 'ENTRADA/*.pdf'

    pdf_files = glob.glob(dir_entrada)

    for pdf_base in pdf_files:
        print()
        print('MODIFICANDO PDF ',pdf_base)
        pdf = PdfReader(pdf_base)
        pdf_salida = PdfWriter()
        try:
            file_name = pdf_base.split('/')[1]
        except:
            file_name = pdf_base.split( '\\' )[1]
        path_salida = 'SALIDA/' + file_name
        #print(path_salida)

        #print(len(pdf.pages))
        for num_pagina in range(0,len(pdf.pages)):
            page_base = pdf.pages[num_pagina]
            if num_pagina%2 == 1:
                page_base.rotate(ANGULO)
                vert = CORRECCION_EN_PIXELES_VERTICAL
                hor = CORRECCION_EN_PIXELES_HORIZONTAL
                if ANGULO == 180:
                    vert = - CORRECCION_EN_PIXELES_VERTICAL
                    hor = - CORRECCION_EN_PIXELES_HORIZONTAL
                transformation = Transformation().translate(tx=hor,ty=vert)
                page_base.add_transformation(transformation)
                
            
            pdf_salida.add_page(page_base)
        
        with open(path_salida,'wb') as pdf_s:
            pdf_salida.write(pdf_s)
            print('SALVANDO PDF ',path_salida)

    print()        


