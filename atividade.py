from datetime import datetime

class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self._id = id
        self._nome = nome
        self._email = email
        self._fone = fone

    def __str__(self):
        return f"Cliente[ID: {self._id}, Nome: {self._nome}, Email: {self._email}, Fone: {self._fone}]"

    # Getters
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_fone(self):
        return self._fone

    # Setters
    def set_nome(self, nome: str):
        self._nome = nome

    def set_email(self, email: str):
        self._email = email

    def set_fone(self, fone: str):
        self._fone = fone


class Horario:
    def __init__(self, id: int, data: datetime, confirmado: bool, id_cliente: int, id_servico: int):
        self._id = id
        self._data = data
        self._confirmado = confirmado
        self._id_cliente = id_cliente
        self._id_servico = id_servico

    def __str__(self):
        return (f"Horario[ID: {self._id}, Data: {self._data}, Confirmado: {self._confirmado}, "
                f"ID Cliente: {self._id_cliente}, ID Serviço: {self._id_servico}]")

    # Getters
    def get_id(self):
        return self._id

    def get_data(self):
        return self._data

    def get_confirmado(self):
        return self._confirmado

    def get_id_cliente(self):
        return self._id_cliente

    def get_id_servico(self):
        return self._id_servico

    # Setters
    def set_data(self, data: datetime):
        self._data = data

    def set_confirmado(self, confirmado: bool):
        self._confirmado = confirmado

    def set_id_cliente(self, id_cliente: int):
        self._id_cliente = id_cliente

    def set_id_servico(self, id_servico: int):
        self._id_servico = id_servico


class Servico:
    def __init__(self, id: int, descricao: str, valor: float, duracao: int):
        self._id = id
        self._descricao = descricao
        self._valor = valor
        self._duracao = duracao

    def __str__(self):
        return (f"Servico[ID: {self._id}, Descrição: {self._descricao}, Valor: {self._valor}, "
                f"Duração: {self._duracao} minutos]")

    # Getters
    def get_id(self):
        return self._id

    def get_descricao(self):
        return self._descricao

    def get_valor(self):
        return self._valor

    def get_duracao(self):
        return self._duracao

    # Setters
    def set_descricao(self, descricao: str):
        self._descricao = descricao

    def set_valor(self, valor: float):
        self._valor = valor

    def set_duracao(self, duracao: int):
        self._duracao = duracao

import json
from typing import List, Optional
from datetime import datetime

# Classes de modelo
class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f"Cliente[ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Fone: {self.fone}]"

    def to_dict(self):
        return vars(self)


class Horario:
    def __init__(self, id: int, data: datetime, confirmado: bool, id_cliente: int, id_servico: int):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.id_cliente = id_cliente
        self.id_servico = id_servico

    def __str__(self):
        return (f"Horario[ID: {self.id}, Data: {self.data}, Confirmado: {self.confirmado}, "
                f"ID Cliente: {self.id_cliente}, ID Serviço: {self.id_servico}]")

    def to_dict(self):
        return {
            "id": self.id,
            "data": self.data.isoformat(),
            "confirmado": self.confirmado,
            "id_cliente": self.id_cliente,
            "id_servico": self.id_servico
        }


class Servico:
    def __init__(self, id: int, descricao: str, valor: float, duracao: int):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.duracao = duracao

    def __str__(self):
        return (f"Servico[ID: {self.id}, Descrição: {self.descricao}, Valor: {self.valor}, "
                f"Duração: {self.duracao} minutos]")

    def to_dict(self):
        return vars(self)


# Classes de persistência
class Clientes:
    objetos: List[Cliente] = []

    @staticmethod
    def inserir(obj: Cliente):
        Clientes.objetos.append(obj)

    @staticmethod
    def listar() -> List[Cliente]:
        return Clientes.objetos

    @staticmethod
    def listar_id(id: int) -> Optional[Cliente]:
        for cliente in Clientes.objetos:
            if cliente.id == id:
                return cliente
        return None

    @staticmethod
    def atualizar(obj: Cliente):
        for i, cliente in enumerate(Clientes.objetos):
            if cliente.id == obj.id:
                Clientes.objetos[i] = obj
                return

    @staticmethod
    def excluir(id: int):
        Clientes.objetos = [cliente for cliente in Clientes.objetos if cliente.id != id]

    @staticmethod
    def abrir(caminho: str):
        try:
            with open(caminho, 'r') as file:
                dados = json.load(file)
                Clientes.objetos = [Cliente(**dado) for dado in dados]
        except FileNotFoundError:
            Clientes.objetos = []

    @staticmethod
    def salvar(caminho: str):
        with open(caminho, 'w') as file:
            json.dump([cliente.to_dict() for cliente in Clientes.objetos], file, indent=4)


class Horarios:
    objetos: List[Horario] = []

    @staticmethod
    def inserir(obj: Horario):
        Horarios.objetos.append(obj)

    @staticmethod
    def listar() -> List[Horario]:
        return Horarios.objetos

    @staticmethod
    def listar_id(id: int) -> Optional[Horario]:
        for horario in Horarios.objetos:
            if horario.id == id:
                return horario
        return None

    @staticmethod
    def atualizar(obj: Horario):
        for i, horario in enumerate(Horarios.objetos):
            if horario.id == obj.id:
                Horarios.objetos[i] = obj
                return

    @staticmethod
    def excluir(id: int):
        Horarios.objetos = [horario for horario in Horarios.objetos if horario.id != id]

    @staticmethod
    def abrir(caminho: str):
        try:
            with open(caminho, 'r') as file:
                dados = json.load(file)
                Horarios.objetos = [Horario(**{
                    **dado,
                    'data': datetime.fromisoformat(dado['data'])
                }) for dado in dados]
        except FileNotFoundError:
            Horarios.objetos = []

    @staticmethod
    def salvar(caminho: str):
        with open(caminho, 'w') as file:
            json.dump([horario.to_dict() for horario in Horarios.objetos], file, indent=4)


class Servicos:
    objetos: List[Servico] = []

    @staticmethod
    def inserir(obj: Servico):
        Servicos.objetos.append(obj)

    @staticmethod
    def listar() -> List[Servico]:
        return Servicos.objetos

    @staticmethod
    def listar_id(id: int) -> Optional[Servico]:
        for servico in Servicos.objetos:
            if servico.id == id:
                return servico
        return None

    @staticmethod
    def atualizar(obj: Servico):
        for i, servico in enumerate(Servicos.objetos):
            if servico.id == obj.id:
                Servicos.objetos[i] = obj
                return

    @staticmethod
    def excluir(id: int):
        Servicos.objetos = [servico for servico in Servicos.objetos if servico.id != id]

    @staticmethod
    def abrir(caminho: str):
        try:
            with open(caminho, 'r') as file:
                dados = json.load(file)
                Servicos.objetos = [Servico(**dado) for dado in dados]
        except FileNotFoundError:
            Servicos.objetos = []

    @staticmethod
    def salvar(caminho: str):
        with open(caminho, 'w') as file:
            json.dump([servico.to_dict() for servico in Servicos.objetos], file, indent=4)
from datetime import datetime

class View:

    # Métodos para Clientes
    @staticmethod
    def cliente_listar() -> List[Cliente]:
        return Clientes.listar()

    @staticmethod
    def cliente_inserir(nome: str, email: str, fone: str):
        novo_cliente = Cliente(id=len(Clientes.objetos) + 1, nome=nome, email=email, fone=fone)
        Clientes.inserir(novo_cliente)

    @staticmethod
    def cliente_atualizar(id: int, nome: str, email: str, fone: str):
        cliente = Clientes.listar_id(id)
        if cliente:
            cliente.nome = nome
            cliente.email = email
            cliente.fone = fone
            Clientes.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id: int):
        Clientes.excluir(id)

    # Métodos para Horários
    @staticmethod
    def horario_listar() -> List[Horario]:
        return Horarios.listar()

    @staticmethod
    def horario_inserir(data: datetime, confirmado: bool, id_cliente: int, id_servico: int):
        novo_horario = Horario(id=len(Horarios.objetos) + 1, data=data, confirmado=confirmado,
                               id_cliente=id_cliente, id_servico=id_servico)
        Horarios.inserir(novo_horario)

    @staticmethod
    def horario_atualizar(id: int, data: datetime, confirmado: bool, id_cliente: int, id_servico: int):
        horario = Horarios.listar_id(id)
        if horario:
            horario.data = data
            horario.confirmado = confirmado
            horario.id_cliente = id_cliente
            horario.id_servico = id_servico
            Horarios.atualizar(horario)

    @staticmethod
    def horario_excluir(id: int):
        Horarios.excluir(id)

    @staticmethod
    def horario_abrir_agenda(data: datetime, hora_inicio: int, hora_fim: int, intervalo: int):
        horarios_disponiveis = []
        hora_atual = hora_inicio
        while hora_atual < hora_fim:
            data_horario = data.replace(hour=hora_atual, minute=0)
            horarios_disponiveis.append(data_horario)
            hora_atual += intervalo
        return horarios_disponiveis

    # Métodos para Serviços
    @staticmethod
    def servico_listar() -> List[Servico]:
        return Servicos.listar()

    @staticmethod
    def servico_inserir(descricao: str, valor: float, duracao: int):
        novo_servico = Servico(id=len(Servicos.objetos) + 1, descricao=descricao, valor=valor, duracao=duracao)
        Servicos.inserir(novo_servico)

    @staticmethod
    def servico_atualizar(id: int, descricao: str, valor: float, duracao: int):
        servico = Servicos.listar_id(id)
        if servico:
            servico.descricao = descricao
            servico.valor = valor
            servico.duracao = duracao
            Servicos.atualizar(servico)

    @staticmethod
    def servico_excluir(id: int):
        Servicos.excluir(id)

import streamlit as st
from datetime import datetime
from typing import List

# Importando as classes e métodos
# from your_module import View, Cliente, Horario, Servico

st.title("Sistema de Gerenciamento")

menu = ["Clientes", "Horários", "Serviços"]
choice = st.sidebar.selectbox("Selecione a opção", menu)

# Página de Clientes
if choice == "Clientes":
    st.header("Gerenciamento de Clientes")

    action = st.selectbox("Ação", ["Listar", "Inserir", "Atualizar", "Excluir"])

    if action == "Listar":
        clientes = View.cliente_listar()
        for cliente in clientes:
            st.write(cliente)

    elif action == "Inserir":
        st.subheader("Inserir novo Cliente")
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        fone = st.text_input("Telefone")

        if st.button("Inserir Cliente"):
            View.cliente_inserir(nome, email, fone)
            st.success("Cliente inserido com sucesso!")

    elif action == "Atualizar":
        st.subheader("Atualizar Cliente")
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
        nome = st.text_input("Novo Nome")
        email = st.text_input("Novo Email")
        fone = st.text_input("Novo Telefone")

        if st.button("Atualizar Cliente"):
            View.cliente_atualizar(id_cliente, nome, email, fone)
            st.success("Cliente atualizado com sucesso!")

    elif action == "Excluir":
        st.subheader("Excluir Cliente")
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)

        if st.button("Excluir Cliente"):
            View.cliente_excluir(id_cliente)
            st.success("Cliente excluído com sucesso!")

# Página de Horários
elif choice == "Horários":
    st.header("Gerenciamento de Horários")

    action = st.selectbox("Ação", ["Listar", "Inserir", "Atualizar", "Excluir", "Abrir Agenda"])

    if action == "Listar":
        horarios = View.horario_listar()
        for horario in horarios:
            st.write(horario)

    elif action == "Inserir":
        st.subheader("Inserir novo Horário")
        data = st.date_input("Data")
        hora = st.time_input("Hora")
        data_horario = datetime.combine(data, hora)
        confirmado = st.checkbox("Confirmado")
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
        id_servico = st.number_input("ID do Serviço", min_value=1, step=1)

        if st.button("Inserir Horário"):
            View.horario_inserir(data_horario, confirmado, id_cliente, id_servico)
            st.success("Horário inserido com sucesso!")

    elif action == "Atualizar":
        st.subheader("Atualizar Horário")
        id_horario = st.number_input("ID do Horário", min_value=1, step=1)
        data = st.date_input("Nova Data")
        hora = st.time_input("Nova Hora")
        data_horario = datetime.combine(data, hora)
        confirmado = st.checkbox("Confirmado")
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
        id_servico = st.number_input("ID do Serviço", min_value=1, step=1)

        if st.button("Atualizar Horário"):
            View.horario_atualizar(id_horario, data_horario, confirmado, id_cliente, id_servico)
            st.success("Horário atualizado com sucesso!")

    elif action == "Excluir":
        st.subheader("Excluir Horário")
        id_horario = st.number_input("ID do Horário", min_value=1, step=1)

        if st.button("Excluir Horário"):
            View.horario_excluir(id_horario)
            st.success("Horário excluído com sucesso!")

    elif action == "Abrir Agenda":
        st.subheader("Abrir Agenda do Dia")
        data = st.date_input("Data")
        hora_inicio = st.number_input("Hora Início", min_value=0, max_value=23, step=1)
        hora_fim = st.number_input("Hora Fim", min_value=0, max_value=23, step=1)
        intervalo = st.number_input("Intervalo (em horas)", min_value=1, max_value=12, step=1)

        if st.button("Abrir Agenda"):
            horarios_disponiveis = View.horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo)
            for horario in horarios_disponiveis:
                st.write(horario)

# Página de Serviços
elif choice == "Serviços":
    st.header("Gerenciamento de Serviços")

    action = st.selectbox("Ação", ["Listar", "Inserir", "Atualizar", "Excluir"])

    if action == "Listar":
        servicos = View.servico_listar()
        for servico in servicos:
            st.write(servico)

    elif action == "Inserir":
        st.subheader("Inserir novo Serviço")
        descricao = st.text_input("Descrição")
        valor = st.number_input("Valor", min_value=0.0, format="%.2f")
        duracao = st.number_input("Duração (em minutos)", min_value=1, step=1)

        if st.button("Inserir Serviço"):
            View.servico_inserir(descricao, valor, duracao)
            st.success("Serviço inserido com sucesso!")

    elif action == "Atualizar":
        st.subheader("Atualizar Serviço")
        id_servico = st.number_input("ID do Serviço", min_value=1, step=1)
        descricao = st.text_input("Nova Descrição")
        valor = st.number_input("Novo Valor", min_value=0.0, format="%.2f")
        duracao = st.number_input("Nova Duração (em minutos)", min_value=1, step=1)

        if st.button("Atualizar Serviço"):
            View.servico_atualizar(id_servico, descricao, valor, duracao)
            st.success("Serviço atualizado com sucesso!")

    elif action == "Excluir":
        st.subheader("Excluir Serviço")
        id_servico = st.number_input("ID do Serviço", min_value=1, step=1)

        if st.button("Excluir Serviço"):
            View.servico_excluir(id_servico)
            st.success("Serviço excluído com sucesso!")
