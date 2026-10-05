#Sistema de vendas
#Secao cadastrar vendas
    #campo vendedor
    #campo produto
    #campo quantidade
    #campo valor
    #botao cadastrar vendas
        #quando clicar botao -> adicionar venda na tabela
#Secao vendas cadastradas
    #tabela com vendas
#Secao dashbord
    #card/metrica -> faturamento total
    #grafico de barra/coluna -> venda por vendedor
    #grafico de pizza -> venda por produtor


import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv('vendas.csv')

# Passo 1: Criar a tela do sistema
st.write('# Sistema de Vendas')

# Passo 2: Criar o formulário de cadastro
# Passo 3: Salvar a venda na base de dados
st.sidebar.write('## Cadrastrar Vendas')
data = st.sidebar.date_input('Data')
vendedor = st.sidebar.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla'])
produto = st.sidebar.selectbox('Produto', ['Celular', 'Notebook', 'Fone'])
quantidade = st.sidebar.number_input('Quantidade', step=1)
valor = st.sidebar.number_input('Valor')
botao_cadastrar = st.sidebar.button('Cadastrar Venda')
# logica de cadastro
if botao_cadastrar:
    if valor <= 0:
        st.warning('Valor vazio')
    else:    
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv('vendas.csv', index=False)
        st.success('Venda cadastrada!!')

# Passo 4: Mostrar a base de dados na tela
st.write('## Vendas Cadastradas')
st.dataframe(tabela_vendas)


# Passo 5: Criar o dashboard com os gráficos
st.write('## Dashbord')

#Card - faturamento
faturamento = tabela_vendas['valor'].sum()
st.metric('Faturamento Total', f'R$ {faturamento:.2f}')

#Grafico - venda por vendedor
grafico1 = px.bar(tabela_vendas, x='vendedor', y='valor', color='produto')
st.plotly_chart(grafico1)

#Grafico - venda por produto
grafico2 = px.pie(tabela_vendas, names='produtos', values='valor', hole=0.3)
st.plotly_chart(grafico2)













