import streamlit as st
import pandas as pd
import plotly.express as px

# Função para carregar os dados
@st.cache_data
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Carregar dados do Excel
file_path = 'dados_fgv_agro.xlsx'
data = load_data(file_path)

# Título do dashboard
st.title('Observatório de Bioeconomia na Amazônia')

# Sumário interativo
st.sidebar.title('Sumário')
st.sidebar.header('Navegação')
st.sidebar.markdown('<span class="iconify" data-icon="fa-solid:eye"></span> [Visualização dos Dados](#visualizacao-dos-dados)', unsafe_allow_html=True)
st.sidebar.markdown('<span class="iconify" data-icon="fa-solid:chart-line"></span> [Análise Temporal](#analise-temporal)', unsafe_allow_html=True)
st.sidebar.markdown('<span class="iconify" data-icon="fa-solid:chart-bar"></span> [Estatísticas Descritivas](#estatisticas-descritivas)', unsafe_allow_html=True)
st.sidebar.markdown('<span class="iconify" data-icon="fa-solid:globe-americas"></span> [Distribuição Geográfica](#distribuicao-geografica)', unsafe_allow_html=True)
st.sidebar.markdown('<span class="iconify" data-icon="fa-solid:comment"></span> [Comentários](#comentarios)', unsafe_allow_html=True)

# CSS para ícones
st.markdown("""
    <style>
        .iconify {
            margin-right: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Seção 1: Visualização dos dados
st.header('Visualização dos Dados')
st.markdown('<a name="visualizacao-dos-dados"></a>', unsafe_allow_html=True)

# Exemplo de gráfico de dispersão para correlação entre setores
fig_scatter = px.scatter(data, x='Agricultura', y='Pecuária', color='Trimestre', title='Correlação entre Agricultura e Pecuária')
st.plotly_chart(fig_scatter)

# Seção 2: Análise Temporal
st.header('Análise Temporal')
st.markdown('<a name="analise-temporal"></a>', unsafe_allow_html=True)

# Gráfico de linha para mostrar a evolução do número de empregados ao longo do tempo em diferentes setores
fig_line = px.line(data, x='Ano', y=['Agricultura', 'Pecuária', 'Agropecuária'], title='Evolução do Número de Empregados por Setor')
st.plotly_chart(fig_line)

# Seção 3: Estatísticas Descritivas
st.header('Estatísticas Descritivas')
st.markdown('<a name="estatisticas-descritivas"></a>', unsafe_allow_html=True)

# Mostrar estatísticas descritivas resumidas
st.write(data.describe())

# Seção 4: Mapa de distribuição geográfica (exemplo de como seria, se houver informações de localização geográfica)
st.header('Distribuição Geográfica')
st.markdown('<a name="distribuicao-geografica"></a>', unsafe_allow_html=True)

# Seus dados não incluem informações de localização geográfica, então esta seção é apenas um exemplo
st.write('Não há dados de localização geográfica disponíveis para visualização.')

# Seção: Gráfico de barras
st.header('Comparação entre Produtos Alimentícios e Não Alimentícios')

# Agrupando os dados por ano e calculando a soma dos valores para produtos alimentícios e não alimentícios
data_grouped = data.groupby('Ano').agg({'Produtos Alimentícios': 'sum', 'Produtos Não-Alimentícios': 'sum'}).reset_index()

# Criando um gráfico de barras para comparar produtos alimentícios e não alimentícios ao longo dos anos
fig_bar = px.bar(data_grouped, x='Ano', y=['Produtos Alimentícios', 'Produtos Não-Alimentícios'], 
                 title='Comparação entre Produtos Alimentícios e Não Alimentícios ao Longo dos Anos')
st.plotly_chart(fig_bar)

# Seção 5: Comentários ou informações adicionais
st.header('Comentários')
st.markdown('<a name="comentarios"></a>', unsafe_allow_html=True)

# Adicione qualquer informação adicional que você gostaria de compartilhar com os usuários
st.write('Este é um observatório de dados simples para visualizar informações sobre a bioeconomia na Amazônia. Sinta-se à vontade para explorar!')
