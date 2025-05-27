import streamlit as st
import tempfile
import os
from core import process_xls
from utils import write_csv_lines

def write_csv_download(rows, total_cols, label):
    lines = write_csv_lines(rows, total_cols)
    output = '\n'.join(lines)
    st.download_button(
        label=label,
        data=output,
        file_name=label.replace(' ', '_').lower() + '.csv',
        mime='text/csv'
    )

st.title('Generador de CSV de Estadísticas de Béisbol')
st.write('Sube un archivo .xls con las hojas requeridas para generar los CSVs de visitante y local.')

uploaded_file = st.file_uploader('Sube un archivo .xls', type=['xls'])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xls') as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    try:
        visitor_rows, visitor_total_cols, home_rows, home_total_cols = process_xls(tmp_path)
        write_csv_download(visitor_rows, visitor_total_cols, 'Descargar CSV Visitante')
        write_csv_download(home_rows, home_total_cols, 'Descargar CSV Local')
    except Exception as e:
        st.error(f'Error procesando el archivo: {e}')
    finally:
        os.remove(tmp_path)
