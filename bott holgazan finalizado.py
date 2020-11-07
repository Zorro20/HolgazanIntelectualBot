#Importamos las librerias y modulos
import logging
import telebot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#Habilitar el registro
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#Definimos algunos controladores de comandos
def start(update, context):
    "" "Envía un mensaje cuando se emite el comando /hola." ""
    update.message.reply_text('Hola!! gracias por usarme :), ingresa el comando /materias para ver las opciones!!')
#COMANDO O MENU DE MATERIAS
def materias(update, context):
    update.message.reply_text( """Te puedo ayudar en las siguientes materias del 2do semestre:
1-/AnalisisMatematicoI
2-/AnalisisMatematicoII
3-/AlgebraLinealI
4-/AlgebraLinealII
5-/QuimicaI
6-/FisicaI
7-/FundamentosdeInformatica
8-/IntroduccionalaProgramacion 
9-/SistemasdeRepresentacion
""")
#MATERIA DE ANALISIS MATEMATICO
def AnalisismatematicoII(update, context):
    update.message.reply_text("""En Analisis Matematico puedo ayudarte en:
-/Teoria1
-/Libros1
-/TrabajosPracticos1
-/EjemplosdeParcialesFinales1""")
def Teoria1(update,context):
    update.message.reply_text("""Tengo 3 unidades que te puedo brindar:
UNIDAD 1: Aplicaciones de calculo diferencial:
LINK: https://drive.google.com/file/d/1WUQBGiwvnZ-qzAnWOav4TFHQLiJFn105/view?usp=sharing """)
    update.message.reply_text("""UNIDAD 2: 1ra parte 2da parte 3era parte:
LINK:https://drive.google.com/file/d/1pY_WmpC1Iz46vTzPHrfa-QTH1Ps6VFC_/view?usp=sharing""")
    update.message.reply_text("""UNIDAD 3: Sucesiones y Series:
LINK: https://drive.google.com/file/d/1Q4kZVcGDNl7xMCFQ4qW30zirtqjPjG23/view?usp=sharing""")
def Libros1(update, context):
    update.message.reply_text("""Tengo 3 libros que te ayudaran seguro!!!:
lIBRO1:Calculo de una variable Thomas: 
LINK: https://drive.google.com/file/d/1gTX3qw3Z8DC0cnrPms-5iMcq0S5Ca09F/view?usp=sharing """)
    update.message.reply_text("""LIBRO 2: Leithold Louis-El calculo (7ed)
LINK: https://drive.google.com/file/d/1f_PbPObsFiBaABn0LZ0dI4UtXRkujNmX/view?usp=sharing """)
    update.message.reply_text("""LIBRO 3:Cálculo de una Variable - 7ma Edición de James Stewart
LINK: https://drive.google.com/file/d/1hsto2NFkbrj_FeNIS50xEqyWc47ZL3MG/view?usp=sharing """)
def TrabajosPracticos1(update, context):
    update.message.reply_text("""Tengo 5 trabajos practicos que te interesaran¿Cual te gustaria revizar?:
-/TP1- APLICACIONES DE LA DERIVADA
-/TP2- INTEGRALES INDEFINIDAS
-/TP3- INTEGRALES DEFINIDAS – INTEGRALES IMPROPIAS - ECUACIONES DIFERENCIALES
-/TP4- APLICACIONES DE LA INTEGRAL
-/TP5- SUCESIONES – SERIES – SERIES DE POTENCIA """)
def TP1(update,context):
    update.message.reply_text("""LINK: https://drive.google.com/file/d/1Hc2haikwnvijtqRsJ_6-TRdSvE5GosBc/view?usp=sharing
RESOLUCIÓN:
LINK: https://drive.google.com/file/d/1wYw6iGOcWqnZY7HFaUNkpdLpiUrmr0JZ/view?usp=sharing""")
def TP2(update,context):
    update.message.reply_text("""TP2:
LINK: https://drive.google.com/file/d/1S72diG6-DMEtLpgO8o7ncOx6XAwQY0KU/view?usp=sharing
RESOLUCIÓN:
LINK: https://drive.google.com/file/d/18P1Psi2ecAA4shNf6bAzuog8qUpDew4g/view?usp=sharing""")
def TP3(update,context):
    update.message.reply_text("""TP3:
LINK: https://drive.google.com/file/d/1dr3mdD2TUUloerBMOBMjQUx9R9a9TYOQ/view?usp=sharing
RESOLUCIÓN:
LINK: https://drive.google.com/file/d/1WG2UvwW1HRz041oFReDsCd_u5uEU2R20/view?usp=sharing""")
def TP4(update,context):
    update.message.reply_text("""TP4:
LINK: https://drive.google.com/file/d/1-aMJIkNObOrbHo8ctD29ds52toVc1HNx/view?usp=sharing
RESOLUCIÓN:
LINK: https://drive.google.com/file/d/1DdgOK5Ftjrv0f16aPynDNklVkY-7ggSJ/view?usp=sharing""")
def TP5(update,context):
    update.message.reply_text("""TP5:
LINK: https://drive.google.com/file/d/1CFd7qqk44VS3TynQgqMIk_hC0gl-wsv9/view?usp=sharing
RESOLUCIÓN:
LINK: https://drive.google.com/file/d/1GyYQCg9NmoPgPxGPmPqfaG8C2t8cDsft/view?usp=sharing""")
def EjemplosdeParcialesFinales1(update, context):
    update.message.reply_text("""Tengo 6 modelos de parciales y 2 modelos de examenes finales:
LINK: """)
    
#MATERIA DE ALGEBRA LINEAL II
def AlgebraLinealII(update, context):
    update.message.reply_text("""En Algebra Linela II puedo ayudarte en:
-/Programa2020AL
-/Teoria2
-/EjemplosdeParciales2
-/TrabajosPracticos2
-/Libros2""")
def Programa2020AL(update, context):
    update.message.reply_text("""Programa 2020:
LINK: https://drive.google.com/file/d/1PU6cHBPOqPqEPM0am3LkniYdk7I18rMr/view?usp=sharing""")
def Teoria2(update, context):
    update.message.reply_text(""" Los temas de ALGEBRA LINEAL II según el programa 2020 son (CLASES TEÓRICAS):
1.PRODUCTO VECTORIAL Y PRODUCTO MIXTO
CLASE 1
LINK: https://drive.google.com/file/d/1B1YfeHHavntOioawXQFl2vMs5B6weQTW/view?usp=sharing """)
    update.message.reply_text("""2.ECUCIONES DE RECTAS Y PLANOS:
CLASE 2
LINK: https://drive.google.com/file/d/1cyElVeyb1ENyngru-QHmf4RoczXkp4_T/view?usp=sharing
CLASE 3
LINK: https://drive.google.com/file/d/1Dz5vUSSU4hkq8UUqD3M4J_iPArOOv8kc/view?usp=sharing""")
    update.message.reply_text(""" 3.ESPACIOS Y SUBESPACIOS VECTORIALES:
CLASE4
LINK: https://drive.google.com/file/d/1KqxB1iFKKVvcCNCvZUdrIzVO1yHcpD4I/view?usp=sharing
CLASE 5
LINK: https://drive.google.com/file/d/1ntn_k4oBN7xKVlNEL-d_R4RqJq8CIm6p/view?usp=sharing""")
    update.message.reply_text("""4.TRANSFORMACIONES LINEALES:
CLASE TEÓRICAS:
CLASE 6
LINK: https://drive.google.com/file/d/19xvpZlSpUe94sVfzu2zR7TW3XGzD8T87/view?usp=sharing
CLASE 7
LINK: https://drive.google.com/file/d/1TB3Kp4N6OS4-sh92t9_tLhWbKwu7BiFL/view?usp=sharing
CLASE PRÁCTICA
LINK: https://drive.google.com/file/d/1slEBhdXyxkcY8OuLe-i46PaSYDPkx5wp/view?usp=sharing""")
    update.message.reply_text("""5.PRODUCTO EN ESPACIO VECTORIAL:
CLASE 8
LINK: https://drive.google.com/file/d/1lncMqpbmknHhL4-isuw1-R-oBew3rhWn/view?usp=sharing""")
    update.message.reply_text("""RESÚMEN TEÓRICO:
LINK: https://drive.google.com/file/d/1mdMr-dIdezUh8pyAyq4R4Y49lMClrlFQ/view?usp=sharing""")
def EjemplosdeParciales2(update, context):
    update.message.reply_text("""PARCIALES 2020 del segundo semestre:
PARCIAL 1: CONTENIDO DE TP1 Y TP2
PARACIAL 2: CONTENIDO DE TP3, TP4 Y TP5
LINK: https://drive.google.com/drive/folders/1DOk-aHUoSMh0e3tqCaBwRNWmmipdmJOU?usp=sharing""")
def TrabajosPracticos2(update, context):
    update.message.reply_text("""TRABAJO PRÁCTICO 1
LINK: https://drive.google.com/file/d/1_s301d12E5glE5lLsCOc4oPq8-Bp5-fG/view?usp=sharing""")
    update.message.reply_text("""TRABAJO PRÁCTICO 2
LINK: https://drive.google.com/file/d/1zu95VFWAwvoMjfrSgZTmm4vqzLj3oPj2/view?usp=sharing""")   
    update.message.reply_text("""TRABAJO PRÁCTICO 3
LINK: https://drive.google.com/file/d/1tjbmD2seFYIIN08KRn5cYvCNFz-BtFmd/view?usp=sharing""")
    update.message.reply_text("""TRABAJO PRÁCTICO 4
LINK: https://drive.google.com/file/d/13ZC9a8jE0CPqAJa1Jjbs7E3LcUgfbALk/view?usp=sharing""")
    update.message.reply_text("""TRABAJO PRÁCTICO 5
LINK: https://drive.google.com/file/d/1L_u3QR13F1flxrEN0oi7txplDrK7wroq/view?usp=sharing""")
    update.message.reply_text("""
TRABAJO PRÁCTICO 6
LINK: https://drive.google.com/file/d/1__e2yAea9Ypw5kKcc1wU6-JtypLJQPR3/view?usp=sharing""")
    update.message.reply_text("""TRABAJO PRÁCTICO 7
LINK: https://drive.google.com/file/d/1iUgxnXpXn5qLKgveVVZNxoOQQ0jKLXi1/view?usp=sharing""")
def Libros2(update, context):
    update.message.reply_text("""LIBROS DE ALGEBRA LINEAL II
LINK: https://drive.google.com/file/d/1TFyd3OUgdNuI-is90IBIyPKdvk3J8GTP/view?usp=sharing""")
#MATERIA DE FISICA I
def FisicaI(update, context):
    update.message.reply_text("""En Fisica I puedo ayudarte en:
-/Teoria3
-/Coloquios2020
-/Libros3
-/TrabajosPracticos3""")
def Teoria3 (update, context):
    update.message.reply_text("""En teoria puedo ayudarte en:
/Unidad1F: errores e incertezas
/Unidad2F: Estatica
/Unidad3F: Cinematica
/Unidad4F: Dinamica
/Unidad5F: Trabajo y energia
/Unidad6F: Cantidad de Movimiento
/Unidad7F: Cuerpo rigido
/Unidad8F: Mecanica de los Fluidos""")
def Unidad1F(update, context):
    update.message.reply_text("""Tengo estos dos archivos que te ayudaran seguro!!!:Proceso de Medicion (Teoria) :
LINK: https://drive.google.com/file/d/1QmiNuvLgegDmF-tr1eZ3m5SossFkI-Fc/view?usp=sharing""")
    update.message.reply_text("""Sistemas de Medicion (Power):
LINK: https://drive.google.com/file/d/1LyFkbSdaq72-KXJsFo9SReYsywQLvbOA/view?usp=sharing""")
def Unidad2F(update, context):
    update.message.reply_text(""" Tengo estos dos archivos que te ayudaran seguro!!!:Vectores y Fuerzas(Teoria) :
LINK: https://drive.google.com/file/d/10COmoY3IdUNN5_l8xGtmisF4Knv9wdq6/view?usp=sharing""")
    update.message.reply_text("""Estatica (Teoria):
LINK: https://drive.google.com/file/d/10-SwjgqDEJPm_OvndBqQvDbe1DuCAlRm/view?usp=sharing""")
def Unidad3F(update, context):
    update.message.reply_text("""Tengo estos dos archivos que te ayudaran seguro!!!:Cinematica :
LINK: https://drive.google.com/file/d/1jq9faYr2odEgcBnoJKvCehiXDuCgaKXe/view?usp=sharing""")
    update.message.reply_text("""Cinematica (Power):
LINK: https://drive.google.com/file/d/1TgXAkykqNZn5PussYmawguBIh7CcrzER/view?usp=sharing""")
def Unidad4F(update, context):
    update.message.reply_text("""Tengo estos dos archivos que te ayudaran seguro!!!:Dinamica(Teoria):
LINK:https://drive.google.com/file/d/1cExM5ogCWfajbJd2jp113ff7Vz2_bkmw/view?usp=sharing""")
    update.message.reply_text("""Dinamica(Power):
LINK:https://drive.google.com/file/d/1Y-GpOIALXY4_jwmcR8awMYLdVAkIRa-V/view?usp=sharing""")
def Unidad5F(update, context):
    update.message.reply_text("""Tengo este archivo que te ayudara seguro!!!:Trabajo y Energia(Teoria):
LINK:https://drive.google.com/file/d/1gkh_Ovau6I_PYxWNxfpKwAM_SGqYXQUU/view?usp=sharing""")
def Unidad6F(update, context):
    update.message.reply_text("""Tengo estos dos archivos que te ayudaran seguro!!!:Choque y cantidad de Movimiento (Teoria):
LINK:https://drive.google.com/file/d/1Wt_ON8yUpHYlQFTm1_GKg-IyB5XGquBs/view?usp=sharing""")
    update.message.reply_text("""Sistemas de Particulas-Colisiones:
LINK: https://drive.google.com/file/d/1SPauxMI5-24iP25ouZfcQ6AyIqjmYs9_/view?usp=sharing""")
def Unidad7F(update, context):
    update.message.reply_text("""Tengo estos archivos que te ayudaran seguro!!!:Cuerpo Rigido(Teoria):
LINK:https://drive.google.com/file/d/1OOUVHCCz9K5PI7EWkKN94Zpe5QvUX0H1/view?usp=sharing""")
    update.message.reply_text("""Rotacion(Power):
LINK: https://drive.google.com/file/d/19_BIAXauWtNNu1f-KJdj-978YBXV0K3x/view?usp=sharing""")
def Unidad8F(update, context):
    update.message.reply_text("""Tengo este archivo que te ayudara: Mecanica de los Fluidos (Power):
LINK:https://drive.google.com/file/d/1X89klo4D78m89F4LTP7d_sZTX6Af67dz/view?usp=sharing""")
def Coloquios2020(update,context):
    update.message.reply_text("""Tengo 8 coloquios que se tomaron:
Coloquio Nº1 y su resolucion, corresponde a UNIDAD 1:
LINK: https://drive.google.com/file/d/1to1YRGme_PaOxCOsHClOsl96mz7iXeV3/view?usp=sharing""")
    update.message.reply_text("""Coloquio Nº2 y su resolucion, corresponde a la UNIDAD 2:
LINK: https://drive.google.com/file/d/1ZNjP_hsOcbSGvgZ9ssBX2hFo-nVW-PrO/view?usp=sharing""")
    update.message.reply_text("""Coloquio Nº3 y su resolucion, corresponde a la UNIDAD 3:
LINK:https://drive.google.com/file/d/17R5DQeIy51bfxH3b1Z584WQEGlgHpuqF/view?usp=sharing""")
    update.message.reply_text("""Coloquio Nº4 y su resolucion, corresponde a la UNIDAD 4:
LINK: https://drive.google.com/file/d/1Gta2Ug7-PExe9UIX6zBCpQnNeH3M-rjy/view?usp=sharing""")
    update.message.reply_text("""Colouio Nº5 y su resolucion, corresponde a las UNIDADES 5Y6:
LINK: https://drive.google.com/file/d/1Jbz0y0upp90kacbvCqShCMSjVRdFKCpK/view?usp=sharing""")
    update.message.reply_text("""Colouio Nº6 y su resolucion, corresponde a las UNIDADES 7:
LINK: https://drive.google.com/file/d/1jXwXYiWyNuAIgnBbfFVcI3VZqu-Ejk_7/view?usp=sharing""")
def Libros3(update,context):
    update.message.reply_text("""Te paso algunos libros muy interesantes:
LIBRO1: Fuerza y Equilibrio :
LINK: https://drive.google.com/file/d/1CvFKff-95fPPlZ00uzWYuh41p-qe3ZZV/view?usp=sharing""")
    update.message.reply_text("""LIBRO 2 : Este libro tiene la mayoria de las unidades de la materia:
LINK: https://drive.google.com/file/d/1jv_w5FDw8GuvMbL-Uw3KJcvxtEZJn9U-/view?usp=sharing""")
    update.message.reply_text("""LIBRO 3: Este libro esta muy interesante te lo recomiendo:
LINK: https://drive.google.com/file/d/1xiCGYpsTG5XZfJInGsq1OJA1I122MSa9/view?usp=sharing""")
def TrabajosPracticos3(update,context):
    update.message.reply_text("""Tengo 8 trabajos practicos para practicar: Trabajos Practico Nº1: Errores:
LINK: https://drive.google.com/file/d/1lbPmf65tuVGqK__hmXzTCJCXtOWDbO0z/view?usp=sharing""")
    update.message.reply_text("""Trabajo Practico Nº2: Estatica: 
LINK: https://drive.google.com/file/d/1AJKwNH1DyNzx7kluXjk-WMmEO2PI5YMS/view?usp=sharing""")
    update.message.reply_text("""Trabajo Practico Nº3: Cinematica: 
LINK: https://drive.google.com/file/d/18j2icyTx34A4NQpUwLAjSfoXYOUIDsoJ/view?usp=sharing""")
    update.message.reply_text("""Trabajo Practico Nº4: Dinamica: 
LINK: https://drive.google.com/file/d/1wPMD9hslxJikqfHkfnUCbAgh1Ux6aKoJ/view?usp=sharing""")
    update.message.reply_text("""Trabajo Practico Nº5: Trabajo y Energia: 
LINK: https://drive.google.com/file/d/1RoDNwZZP88B9sab6D1rrrJyh7EFRS7U0/view?usp=sharing""")
    update.message.reply_text("""Trabajo Practico Nº6: Choque y Cantidad de Movimiento: 
LINK: https://drive.google.com/file/d/1SJCzYbyFvo8v_upfTSk0g-IRIXxQduuk/view?usp=sharing""")
    update.message.reply_text("""Trabajo Practico Nº7: Cuerpo Rigido: 
LINK: https://drive.google.com/file/d/124vLQmD-16WmUTCFkbD8TrVqkdwvISJX/view?usp=sharing""")
    update.message.reply_text("""Trabajo Practico Nº8: Fluidos: 
LINK: https://drive.google.com/file/d/1dPyYoucgjMvLfFWoIjtWXYCFeg9bxfp4/view?usp=sharing""")
#MATERIA DE INTRODUCCION A A PROGRAMACION
def IntroduccionalaProgramacion(update, context):
    update.message.reply_text("""En Introduccion a la Programacion puedo ayudarte en:
-/Teoria4
-/EjemplosdeParciales4
-/EjemplosdeRecuperatorios4
-/EjerciciosResuletosTPS4
-/TrabajosPracticos4
-/EjemplosdeEjerciciosVarios4""")
def Teoria4(update, context):
    update.message.reply_text("""Tengo 6 unidades que te resultaran muy interesantes:
/Unidad1IP: Hardware y Software;Arquitectura del Ordenador.
/Unidad2IP: Pseudocodigos, concepto y simbolos; ALGORITMOS.
/Unidad3IP: Programacion resumen de Teoria I; Programacion Resumen de Teoria II.
/Unidad4IP: Ordenamiento de Seleccion Directa-Burbuja-Insercion; Vectores. 
/Unidad5IP: Python Tuplas; Matrices.
/Unidad6IP: Agebra de Broole; Sistemas de Numeracion resumen de teoria I; Sistemas de Numeracion resumen de teoria II """)
def Unidad1IP(update, context):
    update.message.reply_text("""Parte 1: HARDWARE Y SOFTWARE:
LINK:https://drive.google.com/file/d/1cdpqq8PBfXkiA1e2oQZWpZsAOCrE9jo3/view?usp=sharing""")
    update.message.reply_text("""Parte 2: Arquitectura del Ordenador:
LINK:https://drive.google.com/file/d/1kU0ZsxYCqgDliC8Jtd2t7xmRrqEcMeau/view?usp=sharing""")
def Unidad2IP(update, context):
    update.message.reply_text("""Pseudocodigos, concepto y simbolos: 
LINK:https://drive.google.com/file/d/1G1iD0DYu0HZ6Y3zMFnuRyO3lXQMJXLfz/view?usp=sharing""")
    update.message.reply_text("""ALGORITMOS: 
LINK:https://drive.google.com/file/d/11jjLanCrKr4OoAW6rENnEK0RUqx4iGRQ/view?usp=sharing""")
def Unidad3IP(update, context):
    update.message.reply_text("""Programacion resumen de Teoria I
LINK:https://drive.google.com/file/d/17ng-ZrRnj24VYfcDUbk6TUAYOV8FhOtk/view?usp=sharing""")
    update.message.reply_text("""Programacion Resumen de Teoria II 
LINK:https://drive.google.com/file/d/1b9I49xLP8uinp0GJgBQ1pyQ1nFMtySjo/view?usp=sharing""")
def Unidad4IP(update, context):
    update.message.reply_text("""Ordenamiento de Seleccion Directa-Burbuja-Insercion
LINK:https://drive.google.com/file/d/1mUkXGPZxaU-kGPBBxzPfWvQ6Xod1fudB/view?usp=sharing""")
    update.message.reply_text("""Vectores:
LINK:https://drive.google.com/file/d/15ttdxNx1S36YWMkGfleUReikzSzrOX5V/view?usp=sharing""")    
def Unidad5IP(update, context):
    update.message.reply_text("""Python Tuplas:
LINK: https://drive.google.com/file/d/1IVv-JCch_yKaFDIAuxdDEGEFqudo9for/view?usp=sharing""")
    update.message.reply_text("""Matrices:
LINK: https://drive.google.com/file/d/14Hg0QwYIKK_ok-p1JDi_TBrol1wTDcd1/view?usp=sharing""")
def Unidad6IP(update, context):
    update.message.reply_text("""Agebra de Broole:
LINK: https://drive.google.com/file/d/1cqUW9nVcZ-KeoNtSNhEAsmFNfu238oIn/view?usp=sharing""")
    update.message.reply_text("""Sistemas de Numeracion resumen de teoria I:
LINK: https://drive.google.com/file/d/1neXKcCNyX5rtOFNLP-K121RmGyNPOe01/view?usp=sharing""")
    update.message.reply_text("""Sistemas de Numeracion resumen de teoria II:
LINK: https://drive.google.com/file/d/1jxfaHV678aiWftrTN7ojiOfw3vE5TFRh/view?usp=sharing""")
def EjerciciosResueltosTPS4(update, context):
    update.message.reply_text(""" Ejercicios resueltos TPN1:
LINK: https://drive.google.com/file/d/1-oKwk4mcvzihtYu3Y2aOYZ329mJ60BJu/view?usp=sharing""")
    update.message.reply_text(""" Ejercicios resueltos TPN2:
LINK: https://drive.google.com/file/d/1jRp_Uthh0Di96TI1abF-NrHHh2cotNMv/view?usp=sharing""")
def TrabajosPracticos4(update, context):
    update.message.reply_text("""Tengo 4 trabajos Practicos: TP1:
LINK:https://drive.google.com/file/d/1aRi2Rh4cMQCLvhfpOhbfxknoWud5_kVQ/view?usp=sharing""")
    update.message.reply_text("""TP2:
LINK:https://drive.google.com/file/d/1xAvgZFPIF7Ynuo4k94g7sY8_sedoVkHR/view?usp=sharing""")
    update.message.reply_text("""TP3:
LINK:https://drive.google.com/file/d/11yQ2JQP6tNtUO3GcAnZrDKrVOvt-S44S/view?usp=sharing""")
    update.message.reply_text("""TP4:
LINK:https://drive.google.com/file/d/1DVEU9a9WDZv2b3lymbxWE-tqO7wsvDex/view?usp=sharing""")
def EjemplosdeEjerciciosVarios4(update, context):
    update.message.reply_text("""Tengo varios ejercicios echos:
LINK: https://drive.google.com/file/d/1N8JFSrXYeYYFapHYhZeFQ2x1YyZ-RbHz/view?usp=sharing""")
def EjemplosdeParciales4(update, context):
    update.message.reply_text("""Tengo varios ejercicios de parciales:
LINK: https://drive.google.com/file/d/12li1NGtenVKVufUHvywM2vytfArOE4_l/view?usp=sharing""")
#MATERIA: SISTEMAS DE REPRESENTACION
def SistemasdeRepresentacion(update, context):
    "" "Envíe un mensaje cuando se emita el comando / SistemasdeRepresentacion." ""
    update.message.reply_text("""En Sistemas de Representacion puedo ayudarte en:
-/Teoria5
-/Videos5
-/EjemplosdeParciales5
-/EjemplosdeRecuperatorios5
-/Manuales5
-/TrabajosPracticos5""")
def Teoria5(update, context):
    update.message.reply_text("""Tengo un resumen de lo que se vio el año 2020:
LINKhttps://drive.google.com/file/d/1SE9nZHzQnZpgOCjsYS7YvpelkWB-KigR/view?usp=sharing""")
def Videos5(update, context):
    update.message.reply_text("""Metodo Particular de un Pentagono inscrito en una circunferencia:
LINK: https://www.youtube.com/watch?v=YLXqOOxphJc""")
    update.message.reply_text("""Metodo de un Pentagono inscripto en una circunferencia:
LINK: https://www.youtube.com/watch?v=_0vOjP5Wfm4&t=317s""")
    update.message.reply_text("""Metodo General del HEPTAGONO:
LINK: https://www.youtube.com/watch?v=_-zSHLGdFU0""")
    update.message.reply_text("""Metodo Particular del Octogono  inscripto en una circunferencia:
LINK: https://www.youtube.com/watch?v=f90-wnfz_Xs""")
def EjemplosdeParciales5(update, context):
    update.message.reply_text( """Tengo 4 modelos de parciales que pueden ayudarte,
estos se tomaron en el 2020:MODELO 1
LINK: https://drive.google.com/file/d/1Z3RsN02rP7otCJo5ntpE3YH0OuLpxdUN/view?usp=sharing""")
    update.message.reply_text("""MODELO2
LINK: https://drive.google.com/file/d/1iV229eqWVt57iMGQZYt8hoQ0RVrBlaYl/view?usp=sharing""")
    update.message.reply_text("""MODELO 3
LINK: https://drive.google.com/file/d/127DbKEExhF1UL_iRUpfPLYWpM1CFfNRk/view?usp=sharing""")
    update.message.reply_text("""MODELO 4
LINK: https://drive.google.com/file/d/1Gp4LFP69xZDtv4fwMilfGtmlD6WBohU4/view?usp=sharing""")
def EjemplosdeRecuperatorios5(update, context):
    update.message.reply_text("""Tengo 2 modelos de recuperatorios que pueden interesarte,
estos recuperatorios se tomaron en el 2020: MODELO 1 : TEMA 1
LINK: https://drive.google.com/file/d/1YqHgJ-2LxMDxKuAI2cNBpjLO1di2vo-X/view?usp=sharing""")
    update.message.reply_text("""MODELO2 : TEMA 2
LINK: https://drive.google.com/file/d/14WaIUhKUyCR3pBh_kw_-nEcKEtpraD39/view?usp=sharing""")
def Manuales5(update, context):
    update.message.reply_text("""Tengo estos manuales los cuales puedo brindarte:
MANUAL 1: Manual de Normas IRAM
LINK: https://drive.google.com/file/d/16RMcA_s6lesmFAHsk7h56resyltX0geg/preview""")
    update.message.reply_text("""MANUAL 2: Manual Practico de Dibujo Tecnico
Schneider-Sappert ED. Reverte tercera edicion
LINK: https://drive.google.com/file/d/1KAU1Ju1YmCytxq3z-4cHq8w1ZY2uoaV5/view?usp=sharing""")
def TrabajosPracticos5(update, context):
    update.message.reply_text("""Te paso los trabajos Practicos del 1-39 que se tomaron:
LINK: https://drive.google.com/file/d/1SgeOsiDiUVaaxFk5ElpeNez4M570A7k1/preview""")
    
def main():
    """Comienza el bot."""
    # Crea el actualizador y pásamos el token del bot.
    # Asegúrese de establecer use_context = True para usar las nuevas devoluciones de llamada basadas en contexto
    #el Update se conecta y recibe los mensajes.
    updater = Updater("1190968564:AAFtJomakMP9mQettFDX4j5GyCdzhutkrjQ", use_context=True)

    # creamos un dispachador el cual va a crear los comandos del bot.
    dp = updater.dispatcher
    #creamos diferentes comandos para el bot - responde en Telegram
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("materias", materias))
    #MATERIA ANALISIS MATEMATICOII
    dp.add_handler(CommandHandler("AnalisismatematicoII", AnalisismatematicoII))
    dp.add_handler(CommandHandler("Teoria1", Teoria1))
    dp.add_handler(CommandHandler("Libros1", Libros1))
    dp.add_handler(CommandHandler("TrabajosPracticos1", TrabajosPracticos1))
    #MATERIA ALGEBRA LINEAL II
    dp.add_handler(CommandHandler("AlgebraLinealII", AlgebraLinealII))
    dp.add_handler(CommandHandler("Programa2020AL", Programa2020AL))
    dp.add_handler(CommandHandler("Teoria2", Teoria2))
    dp.add_handler(CommandHandler("EjemplosdeParciales2", EjemplosdeParciales2))
    dp.add_handler(CommandHandler("TrabajosPracticos2", TrabajosPracticos2))
    dp.add_handler(CommandHandler("Libros2", Libros2))
    #MATERIA FISICA I 
    dp.add_handler(CommandHandler("FisicaI", FisicaI))
    dp.add_handler(CommandHandler("Teoria3", Teoria3))
    dp.add_handler(CommandHandler("Unidad1F", Unidad1F))
    dp.add_handler(CommandHandler("Unidad2F", Unidad2F))
    dp.add_handler(CommandHandler("Unidad3F", Unidad3F))
    dp.add_handler(CommandHandler("Unidad4F", Unidad4F))
    dp.add_handler(CommandHandler("Unidad5F", Unidad5F))
    dp.add_handler(CommandHandler("Unidad6F", Unidad6F))
    dp.add_handler(CommandHandler("Unidad7F", Unidad7F))
    dp.add_handler(CommandHandler("Unidad8F", Unidad8F))
    dp.add_handler(CommandHandler("Coloquios2020", Coloquios2020))
    dp.add_handler(CommandHandler("Libros3", Libros3))
    dp.add_handler(CommandHandler("TrabajosPracticos3", TrabajosPracticos3))
    #MATERIA INTRODUCCION A LA PROGRAMACION
    dp.add_handler(CommandHandler("IntroduccionalaProgramacion", IntroduccionalaProgramacion))
    dp.add_handler(CommandHandler("Teoria4", Teoria4))
    dp.add_handler(CommandHandler("Unidad1IP", Unidad1IP))
    dp.add_handler(CommandHandler("Unidad2IP", Unidad2IP))
    dp.add_handler(CommandHandler("Unidad3IP", Unidad3IP))
    dp.add_handler(CommandHandler("Unidad4IP", Unidad4IP))
    dp.add_handler(CommandHandler("Unidad5IP", Unidad5IP))
    dp.add_handler(CommandHandler("Unidad6IP", Unidad6IP))
    dp.add_handler(CommandHandler("EjerciciosResueltosTPS", Unidad6IP))
    dp.add_handler(CommandHandler("TrabajosPracticos4", TrabajosPracticos4))
    dp.add_handler(CommandHandler("EjemplosdeEjerciciosVarios4", EjemplosdeEjerciciosVarios4))
    dp.add_handler(CommandHandler("EjemplosdeParciales4", EjemplosdeParciales4))
    #MATERIA SISTEMAS DE REPRESENTACION
    dp.add_handler(CommandHandler("SistemasdeRepresentacion", SistemasdeRepresentacion))
    dp.add_handler(CommandHandler("Teoria5", Teoria5))
    dp.add_handler(CommandHandler("Videos5", Videos5))
    dp.add_handler(CommandHandler("EjemplosdeParciales5", EjemplosdeParciales5))
    dp.add_handler(CommandHandler("EjemplosdeRecuperatorios5", EjemplosdeRecuperatorios5))
    dp.add_handler(CommandHandler("Manuales5", Manuales5))
    dp.add_handler(CommandHandler("TrabajosPracticos5", TrabajosPracticos5))
    # Inicia el bot
    updater.start_polling()

    # Se ejecuta el bot hasta que se presione Ctrl-C en donde el bot se detendra 
    updater.idle()

if __name__ == '__main__':
    main()
