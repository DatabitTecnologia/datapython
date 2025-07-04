from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""
  Rotas do WebService para a classe: Grupo (TB01002)
"""
import grupoDAO


@app.route("/listGrupo/", methods=["POST"])
def listGrupo():
    resultado = grupoDAO.GrupoDAO()
    return resultado.listGrupo(request.json)


@app.route("/dictGrupo/", methods=["POST"])
def dictGrupo():
    resultado = grupoDAO.GrupoDAO()
    return resultado.dictGrupo(request.json)


@app.route("/fieldsGrupo/", methods=["POST"])
def fieldsGrupo():
    resultado = grupoDAO.GrupoDAO()
    return resultado.fieldsGrupo(request.json)


@app.route("/findGrupo/", methods=["POST"])
def findGrupo():
    resultado = grupoDAO.GrupoDAO()
    return resultado.findGrupo(request.json)


@app.route("/GrupoID", methods=["POST"])
def grupoID():
    resultado = grupoDAO.GrupoDAO()
    return resultado.grupoID(request.json)


@app.route("/insGrupo", methods=["POST"])
def insGrupo():
    resultado = grupoDAO.GrupoDAO()
    return resultado.insGrupo(request.json)


@app.route("/updGrupo", methods=["POST"])
def updGrupo():
    resultado = grupoDAO.GrupoDAO()
    return resultado.updGrupo(request.json)


@app.route("/delGrupo", methods=["POST"])
def delGrupo():
    resultado = grupoDAO.GrupoDAO()
    return resultado.delGrupo(request.json)


"""
  Fim rota: Grupo
"""

"""
  Rotas do WebService para a classe: Centro (TB04004)
"""
import centroDAO


@app.route("/listCentro/", methods=["POST"])
def listCentro():
    resultado = centroDAO.CentroDAO()
    return resultado.listCentro(request.json)


@app.route("/dictCentro/", methods=["POST"])
def dictCentro():
    resultado = centroDAO.CentroDAO()
    return resultado.dictCentro(request.json)


@app.route("/fieldsCentro/", methods=["POST"])
def fieldsCentro():
    resultado = centroDAO.CentroDAO()
    return resultado.fieldsCentro(request.json)


@app.route("/findCentro/", methods=["POST"])
def findCentro():
    resultado = centroDAO.CentroDAO()
    return resultado.findCentro(request.json)


@app.route("/CentroID", methods=["POST"])
def centroID():
    resultado = centroDAO.CentroDAO()
    return resultado.centroID(request.json)


@app.route("/insCentro", methods=["POST"])
def insCentro():
    resultado = centroDAO.CentroDAO()
    return resultado.insCentro(request.json)


@app.route("/updCentro", methods=["POST"])
def updCentro():
    resultado = centroDAO.CentroDAO()
    return resultado.updCentro(request.json)


@app.route("/delCentro", methods=["POST"])
def delCentro():
    resultado = centroDAO.CentroDAO()
    return resultado.delCentro(request.json)


"""
  Fim rota: Centro
"""

"""
  Rotas do WebService para a classe: Subcentro (TB04005)
"""
import subcentroDAO


@app.route("/listSubcentro/", methods=["POST"])
def listSubcentro():
    resultado = subcentroDAO.SubcentroDAO()
    return resultado.listSubcentro(request.json)


@app.route("/dictSubcentro/", methods=["POST"])
def dictSubcentro():
    resultado = subcentroDAO.SubcentroDAO()
    return resultado.dictSubcentro(request.json)


@app.route("/fieldsSubcentro/", methods=["POST"])
def fieldsSubcentro():
    resultado = subcentroDAO.SubcentroDAO()
    return resultado.fieldsSubcentro(request.json)


@app.route("/findSubcentro/", methods=["POST"])
def findSubcentro():
    resultado = subcentroDAO.SubcentroDAO()
    return resultado.findSubcentro(request.json)


@app.route("/SubcentroID", methods=["POST"])
def subcentroID():
    resultado = subcentroDAO.SubcentroDAO()
    return resultado.subcentroID(request.json)


@app.route("/insSubcentro", methods=["POST"])
def insSubcentro():
    resultado = subcentroDAO.SubcentroDAO()
    return resultado.insSubcentro(request.json)


@app.route("/updSubcentro", methods=["POST"])
def updSubcentro():
    resultado = subcentroDAO.SubcentroDAO()
    return resultado.updSubcentro(request.json)


@app.route("/delSubcentro", methods=["POST"])
def delSubcentro():
    resultado = subcentroDAO.SubcentroDAO()
    return resultado.delSubcentro(request.json)


"""
  Fim rota: Subcentro
"""

"""
  Rotas do WebService para a classe: Statuspag (TB01102)
"""
import statuspagDAO


@app.route("/listStatuspag/", methods=["POST"])
def listStatuspag():
    resultado = statuspagDAO.StatuspagDAO()
    return resultado.listStatuspag(request.json)


@app.route("/dictStatuspag/", methods=["POST"])
def dictStatuspag():
    resultado = statuspagDAO.StatuspagDAO()
    return resultado.dictStatuspag(request.json)


@app.route("/fieldsStatuspag/", methods=["POST"])
def fieldsStatuspag():
    resultado = statuspagDAO.StatuspagDAO()
    return resultado.fieldsStatuspag(request.json)


@app.route("/findStatuspag/", methods=["POST"])
def findStatuspag():
    resultado = statuspagDAO.StatuspagDAO()
    return resultado.findStatuspag(request.json)


@app.route("/StatuspagID", methods=["POST"])
def statuspagID():
    resultado = statuspagDAO.StatuspagDAO()
    return resultado.statuspagID(request.json)


@app.route("/insStatuspag", methods=["POST"])
def insStatuspag():
    resultado = statuspagDAO.StatuspagDAO()
    return resultado.insStatuspag(request.json)


@app.route("/updStatuspag", methods=["POST"])
def updStatuspag():
    resultado = statuspagDAO.StatuspagDAO()
    return resultado.updStatuspag(request.json)


@app.route("/delStatuspag", methods=["POST"])
def delStatuspag():
    resultado = statuspagDAO.StatuspagDAO()
    return resultado.delStatuspag(request.json)


"""
  Fim rota: Statuspag
"""

"""
  Rotas do WebService para a classe: Conceito (TB01020)
"""
import conceitoDAO


@app.route("/listConceito/", methods=["POST"])
def listConceito():
    resultado = conceitoDAO.ConceitoDAO()
    return resultado.listConceito(request.json)


@app.route("/dictConceito/", methods=["POST"])
def dictConceito():
    resultado = conceitoDAO.ConceitoDAO()
    return resultado.dictConceito(request.json)


@app.route("/fieldsConceito/", methods=["POST"])
def fieldsConceito():
    resultado = conceitoDAO.ConceitoDAO()
    return resultado.fieldsConceito(request.json)


@app.route("/findConceito/", methods=["POST"])
def findConceito():
    resultado = conceitoDAO.ConceitoDAO()
    return resultado.findConceito(request.json)


@app.route("/ConceitoID", methods=["POST"])
def conceitoID():
    resultado = conceitoDAO.ConceitoDAO()
    return resultado.conceitoID(request.json)


@app.route("/insConceito", methods=["POST"])
def insConceito():
    resultado = conceitoDAO.ConceitoDAO()
    return resultado.insConceito(request.json)


@app.route("/updConceito", methods=["POST"])
def updConceito():
    resultado = conceitoDAO.ConceitoDAO()
    return resultado.updConceito(request.json)


@app.route("/delConceito", methods=["POST"])
def delConceito():
    resultado = conceitoDAO.ConceitoDAO()
    return resultado.delConceito(request.json)


"""
  Fim rota: Conceito
"""

"""
  Rotas do WebService para a classe: Empresa (TB01007)
"""
import empresaDAO


@app.route("/listEmpresa/", methods=["POST"])
def listEmpresa():
    resultado = empresaDAO.EmpresaDAO()
    return resultado.listEmpresa(request.json)


@app.route("/dictEmpresa/", methods=["POST"])
def dictEmpresa():
    resultado = empresaDAO.EmpresaDAO()
    return resultado.dictEmpresa(request.json)


@app.route("/fieldsEmpresa/", methods=["POST"])
def fieldsEmpresa():
    resultado = empresaDAO.EmpresaDAO()
    return resultado.fieldsEmpresa(request.json)


@app.route("/findEmpresa/", methods=["POST"])
def findEmpresa():
    resultado = empresaDAO.EmpresaDAO()
    return resultado.findEmpresa(request.json)


@app.route("/EmpresaID", methods=["POST"])
def empresaID():
    resultado = empresaDAO.EmpresaDAO()
    return resultado.empresaID(request.json)


@app.route("/insEmpresa", methods=["POST"])
def insEmpresa():
    resultado = empresaDAO.EmpresaDAO()
    return resultado.insEmpresa(request.json)


@app.route("/updEmpresa", methods=["POST"])
def updEmpresa():
    resultado = empresaDAO.EmpresaDAO()
    return resultado.updEmpresa(request.json)


@app.route("/delEmpresa", methods=["POST"])
def delEmpresa():
    resultado = empresaDAO.EmpresaDAO()
    return resultado.delEmpresa(request.json)


"""
  Fim rota: Empresa
"""

"""
  Rotas do WebService para a classe: Economico (TB01107)
"""
import economicoDAO


@app.route("/listEconomico/", methods=["POST"])
def listEconomico():
    resultado = economicoDAO.EconomicoDAO()
    return resultado.listEconomico(request.json)


@app.route("/dictEconomico/", methods=["POST"])
def dictEconomico():
    resultado = economicoDAO.EconomicoDAO()
    return resultado.dictEconomico(request.json)


@app.route("/fieldsEconomico/", methods=["POST"])
def fieldsEconomico():
    resultado = economicoDAO.EconomicoDAO()
    return resultado.fieldsEconomico(request.json)


@app.route("/findEconomico/", methods=["POST"])
def findEconomico():
    resultado = economicoDAO.EconomicoDAO()
    return resultado.findEconomico(request.json)


@app.route("/EconomicoID", methods=["POST"])
def economicoID():
    resultado = economicoDAO.EconomicoDAO()
    return resultado.economicoID(request.json)


@app.route("/insEconomico", methods=["POST"])
def insEconomico():
    resultado = economicoDAO.EconomicoDAO()
    return resultado.insEconomico(request.json)


@app.route("/updEconomico", methods=["POST"])
def updEconomico():
    resultado = economicoDAO.EconomicoDAO()
    return resultado.updEconomico(request.json)


@app.route("/delEconomico", methods=["POST"])
def delEconomico():
    resultado = economicoDAO.EconomicoDAO()
    return resultado.delEconomico(request.json)


"""
  Fim rota: Economico
"""

"""
  Rotas do WebService para a classe: Nivel (TB01019)
"""
import nivelDAO


@app.route("/listNivel/", methods=["POST"])
def listNivel():
    resultado = nivelDAO.NivelDAO()
    return resultado.listNivel(request.json)


@app.route("/dictNivel/", methods=["POST"])
def dictNivel():
    resultado = nivelDAO.NivelDAO()
    return resultado.dictNivel(request.json)


@app.route("/fieldsNivel/", methods=["POST"])
def fieldsNivel():
    resultado = nivelDAO.NivelDAO()
    return resultado.fieldsNivel(request.json)


@app.route("/findNivel/", methods=["POST"])
def findNivel():
    resultado = nivelDAO.NivelDAO()
    return resultado.findNivel(request.json)


@app.route("/NivelID", methods=["POST"])
def nivelID():
    resultado = nivelDAO.NivelDAO()
    return resultado.nivelID(request.json)


@app.route("/insNivel", methods=["POST"])
def insNivel():
    resultado = nivelDAO.NivelDAO()
    return resultado.insNivel(request.json)


@app.route("/updNivel", methods=["POST"])
def updNivel():
    resultado = nivelDAO.NivelDAO()
    return resultado.updNivel(request.json)


@app.route("/delNivel", methods=["POST"])
def delNivel():
    resultado = nivelDAO.NivelDAO()
    return resultado.delNivel(request.json)


"""
  Fim rota: Nivel
"""

"""
  Rotas do WebService para a classe: Plano (TB04006)
"""
import planoDAO


@app.route("/listPlano/", methods=["POST"])
def listPlano():
    resultado = planoDAO.PlanoDAO()
    return resultado.listPlano(request.json)


@app.route("/dictPlano/", methods=["POST"])
def dictPlano():
    resultado = planoDAO.PlanoDAO()
    return resultado.dictPlano(request.json)


@app.route("/fieldsPlano/", methods=["POST"])
def fieldsPlano():
    resultado = planoDAO.PlanoDAO()
    return resultado.fieldsPlano(request.json)


@app.route("/findPlano/", methods=["POST"])
def findPlano():
    resultado = planoDAO.PlanoDAO()
    return resultado.findPlano(request.json)


@app.route("/PlanoID", methods=["POST"])
def planoID():
    resultado = planoDAO.PlanoDAO()
    return resultado.planoID(request.json)


@app.route("/insPlano", methods=["POST"])
def insPlano():
    resultado = planoDAO.PlanoDAO()
    return resultado.insPlano(request.json)


@app.route("/updPlano", methods=["POST"])
def updPlano():
    resultado = planoDAO.PlanoDAO()
    return resultado.updPlano(request.json)


@app.route("/delPlano", methods=["POST"])
def delPlano():
    resultado = planoDAO.PlanoDAO()
    return resultado.delPlano(request.json)


"""
  Fim rota: Plano
"""

"""
  Rotas do WebService para a classe: Setor (TB01035)
"""
import setorDAO


@app.route("/listSetor/", methods=["POST"])
def listSetor():
    resultado = setorDAO.SetorDAO()
    return resultado.listSetor(request.json)


@app.route("/dictSetor/", methods=["POST"])
def dictSetor():
    resultado = setorDAO.SetorDAO()
    return resultado.dictSetor(request.json)


@app.route("/fieldsSetor/", methods=["POST"])
def fieldsSetor():
    resultado = setorDAO.SetorDAO()
    return resultado.fieldsSetor(request.json)


@app.route("/findSetor/", methods=["POST"])
def findSetor():
    resultado = setorDAO.SetorDAO()
    return resultado.findSetor(request.json)


@app.route("/SetorID", methods=["POST"])
def setorID():
    resultado = setorDAO.SetorDAO()
    return resultado.setorID(request.json)


@app.route("/insSetor", methods=["POST"])
def insSetor():
    resultado = setorDAO.SetorDAO()
    return resultado.insSetor(request.json)


@app.route("/updSetor", methods=["POST"])
def updSetor():
    resultado = setorDAO.SetorDAO()
    return resultado.updSetor(request.json)


@app.route("/delSetor", methods=["POST"])
def delSetor():
    resultado = setorDAO.SetorDAO()
    return resultado.delSetor(request.json)


"""
  Fim rota: Setor
"""

"""
  Rotas do WebService para a classe: Statusven (TB01021)
"""
import statusvenDAO


@app.route("/listStatusven/", methods=["POST"])
def listStatusven():
    resultado = statusvenDAO.StatusvenDAO()
    return resultado.listStatusven(request.json)


@app.route("/dictStatusven/", methods=["POST"])
def dictStatusven():
    resultado = statusvenDAO.StatusvenDAO()
    return resultado.dictStatusven(request.json)


@app.route("/fieldsStatusven/", methods=["POST"])
def fieldsStatusven():
    resultado = statusvenDAO.StatusvenDAO()
    return resultado.fieldsStatusven(request.json)


@app.route("/findStatusven/", methods=["POST"])
def findStatusven():
    resultado = statusvenDAO.StatusvenDAO()
    return resultado.findStatusven(request.json)


@app.route("/StatusvenID", methods=["POST"])
def statusvenID():
    resultado = statusvenDAO.StatusvenDAO()
    return resultado.statusvenID(request.json)


@app.route("/insStatusven", methods=["POST"])
def insStatusven():
    resultado = statusvenDAO.StatusvenDAO()
    return resultado.insStatusven(request.json)


@app.route("/updStatusven", methods=["POST"])
def updStatusven():
    resultado = statusvenDAO.StatusvenDAO()
    return resultado.updStatusven(request.json)


@app.route("/delStatusven", methods=["POST"])
def delStatusven():
    resultado = statusvenDAO.StatusvenDAO()
    return resultado.delStatusven(request.json)


"""
  Fim rota: Statusven
"""

"""
  Rotas do WebService para a classe: Statusout (TB01073)
"""
import statusoutDAO


@app.route("/listStatusout/", methods=["POST"])
def listStatusout():
    resultado = statusoutDAO.StatusoutDAO()
    return resultado.listStatusout(request.json)


@app.route("/dictStatusout/", methods=["POST"])
def dictStatusout():
    resultado = statusoutDAO.StatusoutDAO()
    return resultado.dictStatusout(request.json)


@app.route("/fieldsStatusout/", methods=["POST"])
def fieldsStatusout():
    resultado = statusoutDAO.StatusoutDAO()
    return resultado.fieldsStatusout(request.json)


@app.route("/findStatusout/", methods=["POST"])
def findStatusout():
    resultado = statusoutDAO.StatusoutDAO()
    return resultado.findStatusout(request.json)


@app.route("/StatusoutID", methods=["POST"])
def statusoutID():
    resultado = statusoutDAO.StatusoutDAO()
    return resultado.statusoutID(request.json)


@app.route("/insStatusout", methods=["POST"])
def insStatusout():
    resultado = statusoutDAO.StatusoutDAO()
    return resultado.insStatusout(request.json)


@app.route("/updStatusout", methods=["POST"])
def updStatusout():
    resultado = statusoutDAO.StatusoutDAO()
    return resultado.updStatusout(request.json)


@app.route("/delStatusout", methods=["POST"])
def delStatusout():
    resultado = statusoutDAO.StatusoutDAO()
    return resultado.delStatusout(request.json)


"""
  Fim rota: Statusout
"""

"""
  Rotas do WebService para a classe: Condicaorec (TB01014)
"""
import condicaorecDAO


@app.route("/listCondicaorec/", methods=["POST"])
def listCondicaorec():
    resultado = condicaorecDAO.CondicaorecDAO()
    return resultado.listCondicaorec(request.json)


@app.route("/dictCondicaorec/", methods=["POST"])
def dictCondicaorec():
    resultado = condicaorecDAO.CondicaorecDAO()
    return resultado.dictCondicaorec(request.json)


@app.route("/fieldsCondicaorec/", methods=["POST"])
def fieldsCondicaorec():
    resultado = condicaorecDAO.CondicaorecDAO()
    return resultado.fieldsCondicaorec(request.json)


@app.route("/findCondicaorec/", methods=["POST"])
def findCondicaorec():
    resultado = condicaorecDAO.CondicaorecDAO()
    return resultado.findCondicaorec(request.json)


@app.route("/CondicaorecID", methods=["POST"])
def condicaorecID():
    resultado = condicaorecDAO.CondicaorecDAO()
    return resultado.condicaorecID(request.json)


@app.route("/insCondicaorec", methods=["POST"])
def insCondicaorec():
    resultado = condicaorecDAO.CondicaorecDAO()
    return resultado.insCondicaorec(request.json)


@app.route("/updCondicaorec", methods=["POST"])
def updCondicaorec():
    resultado = condicaorecDAO.CondicaorecDAO()
    return resultado.updCondicaorec(request.json)


@app.route("/delCondicaorec", methods=["POST"])
def delCondicaorec():
    resultado = condicaorecDAO.CondicaorecDAO()
    return resultado.delCondicaorec(request.json)


"""
  Fim rota: Condicaorec
"""

"""
  Rotas do WebService para a classe: Condicaopag (TB01012)
"""
import condicaopagDAO


@app.route("/listCondicaopag/", methods=["POST"])
def listCondicaopag():
    resultado = condicaopagDAO.CondicaopagDAO()
    return resultado.listCondicaopag(request.json)


@app.route("/dictCondicaopag/", methods=["POST"])
def dictCondicaopag():
    resultado = condicaopagDAO.CondicaopagDAO()
    return resultado.dictCondicaopag(request.json)


@app.route("/fieldsCondicaopag/", methods=["POST"])
def fieldsCondicaopag():
    resultado = condicaopagDAO.CondicaopagDAO()
    return resultado.fieldsCondicaopag(request.json)


@app.route("/findCondicaopag/", methods=["POST"])
def findCondicaopag():
    resultado = condicaopagDAO.CondicaopagDAO()
    return resultado.findCondicaopag(request.json)


@app.route("/CondicaopagID", methods=["POST"])
def condicaopagID():
    resultado = condicaopagDAO.CondicaopagDAO()
    return resultado.condicaopagID(request.json)


@app.route("/insCondicaopag", methods=["POST"])
def insCondicaopag():
    resultado = condicaopagDAO.CondicaopagDAO()
    return resultado.insCondicaopag(request.json)


@app.route("/updCondicaopag", methods=["POST"])
def updCondicaopag():
    resultado = condicaopagDAO.CondicaopagDAO()
    return resultado.updCondicaopag(request.json)


@app.route("/delCondicaopag", methods=["POST"])
def delCondicaopag():
    resultado = condicaopagDAO.CondicaopagDAO()
    return resultado.delCondicaopag(request.json)


"""
  Fim rota: Condicaopag
"""

"""
  Rotas do WebService para a classe: Endereco (TB00012)
"""
import enderecoDAO


@app.route("/listEndereco/", methods=["POST"])
def listEndereco():
    resultado = enderecoDAO.EnderecoDAO()
    return resultado.listEndereco(request.json)


@app.route("/dictEndereco/", methods=["POST"])
def dictEndereco():
    resultado = enderecoDAO.EnderecoDAO()
    return resultado.dictEndereco(request.json)


@app.route("/fieldsEndereco/", methods=["POST"])
def fieldsEndereco():
    resultado = enderecoDAO.EnderecoDAO()
    return resultado.fieldsEndereco(request.json)


@app.route("/findEndereco/", methods=["POST"])
def findEndereco():
    resultado = enderecoDAO.EnderecoDAO()
    return resultado.findEndereco(request.json)


@app.route("/EnderecoID", methods=["POST"])
def enderecoID():
    resultado = enderecoDAO.EnderecoDAO()
    return resultado.enderecoID(request.json)


@app.route("/insEndereco", methods=["POST"])
def insEndereco():
    resultado = enderecoDAO.EnderecoDAO()
    return resultado.insEndereco(request.json)


@app.route("/updEndereco", methods=["POST"])
def updEndereco():
    resultado = enderecoDAO.EnderecoDAO()
    return resultado.updEndereco(request.json)


@app.route("/delEndereco", methods=["POST"])
def delEndereco():
    resultado = enderecoDAO.EnderecoDAO()
    return resultado.delEndereco(request.json)


"""
  Fim rota: Endereco
"""

"""
  Rotas do WebService para a classe: Vendedor (TB01006)
"""
import vendedorDAO


@app.route("/listVendedor/", methods=["POST"])
def listVendedor():
    resultado = vendedorDAO.VendedorDAO()
    return resultado.listVendedor(request.json)


@app.route("/dictVendedor/", methods=["POST"])
def dictVendedor():
    resultado = vendedorDAO.VendedorDAO()
    return resultado.dictVendedor(request.json)


@app.route("/fieldsVendedor/", methods=["POST"])
def fieldsVendedor():
    resultado = vendedorDAO.VendedorDAO()
    return resultado.fieldsVendedor(request.json)


@app.route("/findVendedor/", methods=["POST"])
def findVendedor():
    resultado = vendedorDAO.VendedorDAO()
    return resultado.findVendedor(request.json)


@app.route("/VendedorID", methods=["POST"])
def vendedorID():
    resultado = vendedorDAO.VendedorDAO()
    return resultado.vendedorID(request.json)


@app.route("/insVendedor", methods=["POST"])
def insVendedor():
    resultado = vendedorDAO.VendedorDAO()
    return resultado.insVendedor(request.json)


@app.route("/updVendedor", methods=["POST"])
def updVendedor():
    resultado = vendedorDAO.VendedorDAO()
    return resultado.updVendedor(request.json)


@app.route("/delVendedor", methods=["POST"])
def delVendedor():
    resultado = vendedorDAO.VendedorDAO()
    return resultado.delVendedor(request.json)


"""
  Fim rota: Vendedor
"""

"""
  Rotas do WebService para a classe: Cliente (TB01008)
"""
import clienteDAO


@app.route("/listCliente/", methods=["POST"])
def listCliente():
    resultado = clienteDAO.ClienteDAO()
    return resultado.listCliente(request.json)


@app.route("/dictCliente/", methods=["POST"])
def dictCliente():
    resultado = clienteDAO.ClienteDAO()
    return resultado.dictCliente(request.json)


@app.route("/fieldsCliente/", methods=["POST"])
def fieldsCliente():
    resultado = clienteDAO.ClienteDAO()
    return resultado.fieldsCliente(request.json)


@app.route("/findCliente/", methods=["POST"])
def findCliente():
    resultado = clienteDAO.ClienteDAO()
    return resultado.findCliente(request.json)


@app.route("/ClienteID", methods=["POST"])
def clienteID():
    resultado = clienteDAO.ClienteDAO()
    return resultado.clienteID(request.json)


@app.route("/insCliente", methods=["POST"])
def insCliente():
    resultado = clienteDAO.ClienteDAO()
    return resultado.insCliente(request.json)


@app.route("/updCliente", methods=["POST"])
def updCliente():
    resultado = clienteDAO.ClienteDAO()
    return resultado.updCliente(request.json)


@app.route("/delCliente", methods=["POST"])
def delCliente():
    resultado = clienteDAO.ClienteDAO()
    return resultado.delCliente(request.json)


"""
  Fim rota: Cliente
"""

"""
  Rotas do WebService para a classe: ClienteVW (VW01007)
"""
import clientevwDAO


@app.route("/listClienteVW/", methods=["POST"])
def listClienteVW():
    resultado = clientevwDAO.ClienteVWDAO()
    return resultado.listClienteVW(request.json)


@app.route("/dictClienteVW/", methods=["POST"])
def dictClienteVW():
    resultado = clientevwDAO.ClienteVWDAO()
    return resultado.dictClienteVW(request.json)


@app.route("/fieldsClienteVW/", methods=["POST"])
def fieldsClienteVW():
    resultado = clientevwDAO.ClienteVWDAO()
    return resultado.fieldsClienteVW(request.json)


@app.route("/findClienteVW/", methods=["POST"])
def findClienteVW():
    resultado = clientevwDAO.ClienteVWDAO()
    return resultado.findClienteVW(request.json)


"""
  Fim rota: ClienteVW
"""

"""
  Rotas do WebService para a classe: Servico (TB01005)
"""
import servicoDAO


@app.route("/listServico/", methods=["POST"])
def listServico():
    resultado = servicoDAO.ServicoDAO()
    return resultado.listServico(request.json)


@app.route("/dictServico/", methods=["POST"])
def dictServico():
    resultado = servicoDAO.ServicoDAO()
    return resultado.dictServico(request.json)


@app.route("/fieldsServico/", methods=["POST"])
def fieldsServico():
    resultado = servicoDAO.ServicoDAO()
    return resultado.fieldsServico(request.json)


@app.route("/findServico/", methods=["POST"])
def findServico():
    resultado = servicoDAO.ServicoDAO()
    return resultado.findServico(request.json)


@app.route("/ServicoID", methods=["POST"])
def servicoID():
    resultado = servicoDAO.ServicoDAO()
    return resultado.servicoID(request.json)


@app.route("/insServico", methods=["POST"])
def insServico():
    resultado = servicoDAO.ServicoDAO()
    return resultado.insServico(request.json)


@app.route("/updServico", methods=["POST"])
def updServico():
    resultado = servicoDAO.ServicoDAO()
    return resultado.updServico(request.json)


@app.route("/delServico", methods=["POST"])
def delServico():
    resultado = servicoDAO.ServicoDAO()
    return resultado.delServico(request.json)


"""
  Fim rota: Servico
"""

"""
  Rotas do WebService para a classe: Prestador (TB01017)
"""
import prestadorDAO


@app.route("/listPrestador/", methods=["POST"])
def listPrestador():
    resultado = prestadorDAO.PrestadorDAO()
    return resultado.listPrestador(request.json)


@app.route("/dictPrestador/", methods=["POST"])
def dictPrestador():
    resultado = prestadorDAO.PrestadorDAO()
    return resultado.dictPrestador(request.json)


@app.route("/fieldsPrestador/", methods=["POST"])
def fieldsPrestador():
    resultado = prestadorDAO.PrestadorDAO()
    return resultado.fieldsPrestador(request.json)


@app.route("/findPrestador/", methods=["POST"])
def findPrestador():
    resultado = prestadorDAO.PrestadorDAO()
    return resultado.findPrestador(request.json)


@app.route("/PrestadorID", methods=["POST"])
def prestadorID():
    resultado = prestadorDAO.PrestadorDAO()
    return resultado.prestadorID(request.json)


@app.route("/insPrestador", methods=["POST"])
def insPrestador():
    resultado = prestadorDAO.PrestadorDAO()
    return resultado.insPrestador(request.json)


@app.route("/updPrestador", methods=["POST"])
def updPrestador():
    resultado = prestadorDAO.PrestadorDAO()
    return resultado.updPrestador(request.json)


@app.route("/delPrestador", methods=["POST"])
def delPrestador():
    resultado = prestadorDAO.PrestadorDAO()
    return resultado.delPrestador(request.json)


"""
  Fim rota: Prestador
"""

"""
  Rotas do WebService para a classe: Userclient (TB10001)
"""
import userclientDAO


@app.route("/listUserclient/", methods=["POST"])
def listUserclient():
    resultado = userclientDAO.UserclientDAO()
    return resultado.listUserclient(request.json)


@app.route("/dictUserclient/", methods=["POST"])
def dictUserclient():
    resultado = userclientDAO.UserclientDAO()
    return resultado.dictUserclient(request.json)


@app.route("/fieldsUserclient/", methods=["POST"])
def fieldsUserclient():
    resultado = userclientDAO.UserclientDAO()
    return resultado.fieldsUserclient(request.json)


@app.route("/findUserclient/", methods=["POST"])
def findUserclient():
    resultado = userclientDAO.UserclientDAO()
    return resultado.findUserclient(request.json)


@app.route("/UserclientID", methods=["POST"])
def userclientID():
    resultado = userclientDAO.UserclientDAO()
    return resultado.userclientID(request.json)


@app.route("/insUserclient", methods=["POST"])
def insUserclient():
    resultado = userclientDAO.UserclientDAO()
    return resultado.insUserclient(request.json)


@app.route("/updUserclient", methods=["POST"])
def updUserclient():
    resultado = userclientDAO.UserclientDAO()
    return resultado.updUserclient(request.json)


@app.route("/delUserclient", methods=["POST"])
def delUserclient():
    resultado = userclientDAO.UserclientDAO()
    return resultado.delUserclient(request.json)


"""
  Fim rota: Userclient
"""

"""
  Rotas do WebService para a classe: Paramfield (TB00003)
"""
import paramfieldDAO


@app.route("/listParamfield/", methods=["POST"])
def listParamfield():
    resultado = paramfieldDAO.ParamfieldDAO()
    return resultado.listParamfield(request.json)


@app.route("/dictParamfield/", methods=["POST"])
def dictParamfield():
    resultado = paramfieldDAO.ParamfieldDAO()
    return resultado.dictParamfield(request.json)


@app.route("/fieldsParamfield/", methods=["POST"])
def fieldsParamfield():
    resultado = paramfieldDAO.ParamfieldDAO()
    return resultado.fieldsParamfield(request.json)


@app.route("/findParamfield/", methods=["POST"])
def findParamfield():
    resultado = paramfieldDAO.ParamfieldDAO()
    return resultado.findParamfield(request.json)


@app.route("/ParamfieldID", methods=["POST"])
def paramfieldID():
    resultado = paramfieldDAO.ParamfieldDAO()
    return resultado.paramfieldID(request.json)


@app.route("/insParamfield", methods=["POST"])
def insParamfield():
    resultado = paramfieldDAO.ParamfieldDAO()
    return resultado.insParamfield(request.json)


@app.route("/updParamfield", methods=["POST"])
def updParamfield():
    resultado = paramfieldDAO.ParamfieldDAO()
    return resultado.updParamfield(request.json)


@app.route("/delParamfield", methods=["POST"])
def delParamfield():
    resultado = paramfieldDAO.ParamfieldDAO()
    return resultado.delParamfield(request.json)


"""
  Fim rota: Paramfield
"""

"""
  Rotas do WebService para a classe: Prospect (TB01067)
"""
import prospectDAO


@app.route("/listProspect/", methods=["POST"])
def listProspect():
    resultado = prospectDAO.ProspectDAO()
    return resultado.listProspect(request.json)


@app.route("/dictProspect/", methods=["POST"])
def dictProspect():
    resultado = prospectDAO.ProspectDAO()
    return resultado.dictProspect(request.json)


@app.route("/fieldsProspect/", methods=["POST"])
def fieldsProspect():
    resultado = prospectDAO.ProspectDAO()
    return resultado.fieldsProspect(request.json)


@app.route("/findProspect/", methods=["POST"])
def findProspect():
    resultado = prospectDAO.ProspectDAO()
    return resultado.findProspect(request.json)


@app.route("/ProspectID", methods=["POST"])
def prospectID():
    resultado = prospectDAO.ProspectDAO()
    return resultado.prospectID(request.json)


@app.route("/insProspect", methods=["POST"])
def insProspect():
    resultado = prospectDAO.ProspectDAO()
    return resultado.insProspect(request.json)


@app.route("/updProspect", methods=["POST"])
def updProspect():
    resultado = prospectDAO.ProspectDAO()
    return resultado.updProspect(request.json)


@app.route("/delProspect", methods=["POST"])
def delProspect():
    resultado = prospectDAO.ProspectDAO()
    return resultado.delProspect(request.json)


"""
  Fim rota: Prospect
"""

"""
  Rotas do WebService para a classe: ProspectVW (VW01040)
"""
import prospectvwDAO


@app.route("/listProspectVW/", methods=["POST"])
def listProspectVW():
    resultado = prospectvwDAO.ProspectVWDAO()
    return resultado.listProspectVW(request.json)


@app.route("/dictProspectVW/", methods=["POST"])
def dictProspectVW():
    resultado = prospectvwDAO.ProspectVWDAO()
    return resultado.dictProspectVW(request.json)


@app.route("/fieldsProspectVW/", methods=["POST"])
def fieldsProspectVW():
    resultado = prospectvwDAO.ProspectVWDAO()
    return resultado.fieldsProspectVW(request.json)


@app.route("/findProspectVW/", methods=["POST"])
def findProspectVW():
    resultado = prospectvwDAO.ProspectVWDAO()
    return resultado.findProspectVW(request.json)


@app.route("/ProspectvwID", methods=["POST"])
def prospectvwID():
    resultado = prospectvwDAO.ProspectVWDAO()
    return resultado.prospectvwID(request.json)


"""
  Fim rota: ProspectVW
"""

"""
  Rotas do WebService para a classe: Contato (TB01075)
"""
import contatoDAO


@app.route("/listContato/", methods=["POST"])
def listContato():
    resultado = contatoDAO.ContatoDAO()
    return resultado.listContato(request.json)


@app.route("/dictContato/", methods=["POST"])
def dictContato():
    resultado = contatoDAO.ContatoDAO()
    return resultado.dictContato(request.json)


@app.route("/fieldsContato/", methods=["POST"])
def fieldsContato():
    resultado = contatoDAO.ContatoDAO()
    return resultado.fieldsContato(request.json)


@app.route("/findContato/", methods=["POST"])
def findContato():
    resultado = contatoDAO.ContatoDAO()
    return resultado.findContato(request.json)


@app.route("/ContatoID", methods=["POST"])
def contatoID():
    resultado = contatoDAO.ContatoDAO()
    return resultado.contatoID(request.json)


@app.route("/insContato", methods=["POST"])
def insContato():
    resultado = contatoDAO.ContatoDAO()
    return resultado.insContato(request.json)


@app.route("/updContato", methods=["POST"])
def updContato():
    resultado = contatoDAO.ContatoDAO()
    return resultado.updContato(request.json)


@app.route("/delContato", methods=["POST"])
def delContato():
    resultado = contatoDAO.ContatoDAO()
    return resultado.delContato(request.json)


"""
  Fim rota: Contato
"""

"""
  Rotas do WebService para a classe: Execute
"""
import execSQL


@app.route("/executeSQL/", methods=["POST"])
def ExecuteSQL():
    resultado = execSQL.execSQL()
    return resultado.execSQL(request.json)


"""
  Fim rota: Execute
"""

"""
  Rotas do WebService para a classe: Proposta (TB02102)
"""
import propostaDAO


@app.route("/listProposta/", methods=["POST"])
def listProposta():
    resultado = propostaDAO.PropostaDAO()
    return resultado.listProposta(request.json)


@app.route("/dictProposta/", methods=["POST"])
def dictProposta():
    resultado = propostaDAO.PropostaDAO()
    return resultado.dictProposta(request.json)


@app.route("/fieldsProposta/", methods=["POST"])
def fieldsProposta():
    resultado = propostaDAO.PropostaDAO()
    return resultado.fieldsProposta(request.json)


@app.route("/findProposta/", methods=["POST"])
def findProposta():
    resultado = propostaDAO.PropostaDAO()
    return resultado.findProposta(request.json)


@app.route("/insProposta", methods=["POST"])
def insProposta():
    resultado = propostaDAO.PropostaDAO()
    return resultado.insProposta(request.json)


@app.route("/updProposta", methods=["POST"])
def updProposta():
    resultado = propostaDAO.PropostaDAO()
    return resultado.updProposta(request.json)


@app.route("/delProposta", methods=["POST"])
def delProposta():
    resultado = propostaDAO.PropostaDAO()
    return resultado.delProposta(request.json)


"""
  Fim rota: Proposta
"""

"""
  Rotas do WebService para a classe: PropostaStatus (TB01044)
"""
import propostastatusDAO


@app.route("/listPropostaStatus/", methods=["POST"])
def listPropostaStatus():
    resultado = propostastatusDAO.PropostaStatusDAO()
    return resultado.listPropostaStatus(request.json)


@app.route("/dictPropostaStatus/", methods=["POST"])
def dictPropostaStatus():
    resultado = propostastatusDAO.PropostaStatusDAO()
    return resultado.dictPropostaStatus(request.json)


@app.route("/fieldsPropostaStatus/", methods=["POST"])
def fieldsPropostaStatus():
    resultado = propostastatusDAO.PropostaStatusDAO()
    return resultado.fieldsPropostaStatus(request.json)


@app.route("/findPropostaStatus/", methods=["POST"])
def findPropostaStatus():
    resultado = propostastatusDAO.PropostaStatusDAO()
    return resultado.findPropostaStatus(request.json)


@app.route("/PropostastatusID", methods=["POST"])
def propostastatusID():
    resultado = propostastatusDAO.PropostaStatusDAO()
    return resultado.propostastatusID(request.json)


@app.route("/insPropostaStatus", methods=["POST"])
def insPropostaStatus():
    resultado = propostastatusDAO.PropostaStatusDAO()
    return resultado.insPropostaStatus(request.json)


@app.route("/updPropostaStatus", methods=["POST"])
def updPropostaStatus():
    resultado = propostastatusDAO.PropostaStatusDAO()
    return resultado.updPropostaStatus(request.json)


@app.route("/delPropostaStatus", methods=["POST"])
def delPropostaStatus():
    resultado = propostastatusDAO.PropostaStatusDAO()
    return resultado.delPropostaStatus(request.json)


"""
  Fim rota: PropostaStatus
"""

"""
  Rotas do WebService para a classe: PropostaWorkflow (TB01061)
"""
import propostaworkflowDAO


@app.route("/listPropostaWorkflow/", methods=["POST"])
def listPropostaWorkflow():
    resultado = propostaworkflowDAO.PropostaWorkflowDAO()
    return resultado.listPropostaWorkflow(request.json)


@app.route("/dictPropostaWorkflow/", methods=["POST"])
def dictPropostaWorkflow():
    resultado = propostaworkflowDAO.PropostaWorkflowDAO()
    return resultado.dictPropostaWorkflow(request.json)


@app.route("/fieldsPropostaWorkflow/", methods=["POST"])
def fieldsPropostaWorkflow():
    resultado = propostaworkflowDAO.PropostaWorkflowDAO()
    return resultado.fieldsPropostaWorkflow(request.json)


@app.route("/findPropostaWorkflow/", methods=["POST"])
def findPropostaWorkflow():
    resultado = propostaworkflowDAO.PropostaWorkflowDAO()
    return resultado.findPropostaWorkflow(request.json)


@app.route("/PropostaworkflowID", methods=["POST"])
def propostaworkflowID():
    resultado = propostaworkflowDAO.PropostaWorkflowDAO()
    return resultado.propostaworkflowID(request.json)


@app.route("/insPropostaWorkflow", methods=["POST"])
def insPropostaWorkflow():
    resultado = propostaworkflowDAO.PropostaWorkflowDAO()
    return resultado.insPropostaWorkflow(request.json)


@app.route("/updPropostaWorkflow", methods=["POST"])
def updPropostaWorkflow():
    resultado = propostaworkflowDAO.PropostaWorkflowDAO()
    return resultado.updPropostaWorkflow(request.json)


@app.route("/delPropostaWorkflow", methods=["POST"])
def delPropostaWorkflow():
    resultado = propostaworkflowDAO.PropostaWorkflowDAO()
    return resultado.delPropostaWorkflow(request.json)


"""
  Fim rota: PropostaWorkflow
"""

"""
  Rotas do WebService para a classe: PropostaWorkflowvw (VW01038)
"""
import propostaworkflowvwDAO


@app.route("/listPropostaWorkflowvw/", methods=["POST"])
def listPropostaWorkflowvw():
    resultado = propostaworkflowvwDAO.PropostaWorkflowvwDAO()
    return resultado.listPropostaWorkflowvw(request.json)


@app.route("/dictPropostaWorkflowvw/", methods=["POST"])
def dictPropostaWorkflowvw():
    resultado = propostaworkflowvwDAO.PropostaWorkflowvwDAO()
    return resultado.dictPropostaWorkflowvw(request.json)


@app.route("/fieldsPropostaWorkflowvw/", methods=["POST"])
def fieldsPropostaWorkflowvw():
    resultado = propostaworkflowvwDAO.PropostaWorkflowvwDAO()
    return resultado.fieldsPropostaWorkflowvw(request.json)


"""
  Fim rota: PropostaWorkflowvw
"""

"""
  Rotas do WebService para a classe: PropostaClassifcacao (TB01087)
"""
import propostaclassifcacaoDAO


@app.route("/listPropostaClassifcacao/", methods=["POST"])
def listPropostaClassifcacao():
    resultado = propostaclassifcacaoDAO.PropostaClassifcacaoDAO()
    return resultado.listPropostaClassifcacao(request.json)


@app.route("/dictPropostaClassifcacao/", methods=["POST"])
def dictPropostaClassifcacao():
    resultado = propostaclassifcacaoDAO.PropostaClassifcacaoDAO()
    return resultado.dictPropostaClassifcacao(request.json)


@app.route("/fieldsPropostaClassifcacao/", methods=["POST"])
def fieldsPropostaClassifcacao():
    resultado = propostaclassifcacaoDAO.PropostaClassifcacaoDAO()
    return resultado.fieldsPropostaClassifcacao(request.json)


@app.route("/findPropostaClassifcacao/", methods=["POST"])
def findPropostaClassifcacao():
    resultado = propostaclassifcacaoDAO.PropostaClassifcacaoDAO()
    return resultado.findPropostaClassifcacao(request.json)


@app.route("/PropostaclassifcacaoID", methods=["POST"])
def propostaclassifcacaoID():
    resultado = propostaclassifcacaoDAO.PropostaClassifcacaoDAO()
    return resultado.propostaclassifcacaoID(request.json)


@app.route("/insPropostaClassifcacao", methods=["POST"])
def insPropostaClassifcacao():
    resultado = propostaclassifcacaoDAO.PropostaClassifcacaoDAO()
    return resultado.insPropostaClassifcacao(request.json)


@app.route("/updPropostaClassifcacao", methods=["POST"])
def updPropostaClassifcacao():
    resultado = propostaclassifcacaoDAO.PropostaClassifcacaoDAO()
    return resultado.updPropostaClassifcacao(request.json)


@app.route("/delPropostaClassifcacao", methods=["POST"])
def delPropostaClassifcacao():
    resultado = propostaclassifcacaoDAO.PropostaClassifcacaoDAO()
    return resultado.delPropostaClassifcacao(request.json)


"""
  Fim rota: PropostaClassifcacao
"""

"""
  Rotas do WebService para a classe: Propostavw (VW02121)
"""
import propostavwDAO


@app.route("/listPropostavw/", methods=["POST"])
def listPropostavw():
    resultado = propostavwDAO.PropostavwDAO()
    return resultado.listPropostavw(request.json)


@app.route("/dictPropostavw/", methods=["POST"])
def dictPropostavw():
    resultado = propostavwDAO.PropostavwDAO()
    return resultado.dictPropostavw(request.json)


@app.route("/fieldsPropostavw/", methods=["POST"])
def fieldsPropostavw():
    resultado = propostavwDAO.PropostavwDAO()
    return resultado.fieldsPropostavw(request.json)


@app.route("/findPropostavw/", methods=["POST"])
def findPropostavw():
    resultado = propostavwDAO.PropostavwDAO()
    return resultado.findPropostavw(request.json)


"""
  Fim rota: Propostavw
"""

"""
  Rotas do WebService para a classe: NCM (TB01030)
"""
import ncmDAO


@app.route("/listNCM/", methods=["POST"])
def listNCM():
    resultado = ncmDAO.NCMDAO()
    return resultado.listNCM(request.json)


@app.route("/dictNCM/", methods=["POST"])
def dictNCM():
    resultado = ncmDAO.NCMDAO()
    return resultado.dictNCM(request.json)


@app.route("/fieldsNCM/", methods=["POST"])
def fieldsNCM():
    resultado = ncmDAO.NCMDAO()
    return resultado.fieldsNCM(request.json)


@app.route("/findNCM/", methods=["POST"])
def findNCM():
    resultado = ncmDAO.NCMDAO()
    return resultado.findNCM(request.json)


@app.route("/NCMID", methods=["POST"])
def ncmID():
    resultado = ncmDAO.NCMDAO()
    return resultado.ncmID(request.json)


@app.route("/insNCM", methods=["POST"])
def insNCM():
    resultado = ncmDAO.NCMDAO()
    return resultado.insNCM(request.json)


@app.route("/updNCM", methods=["POST"])
def updNCM():
    resultado = ncmDAO.NCMDAO()
    return resultado.updNCM(request.json)


@app.route("/delNCM", methods=["POST"])
def delNCM():
    resultado = ncmDAO.NCMDAO()
    return resultado.delNCM(request.json)


"""
  Fim rota: NCM
"""

"""
  Rotas do WebService para a classe: Cofins (TB01053)
"""
import cofinsDAO


@app.route("/listCofins/", methods=["POST"])
def listCofins():
    resultado = cofinsDAO.CofinsDAO()
    return resultado.listCofins(request.json)


@app.route("/dictCofins/", methods=["POST"])
def dictCofins():
    resultado = cofinsDAO.CofinsDAO()
    return resultado.dictCofins(request.json)


@app.route("/fieldsCofins/", methods=["POST"])
def fieldsCofins():
    resultado = cofinsDAO.CofinsDAO()
    return resultado.fieldsCofins(request.json)


@app.route("/findCofins/", methods=["POST"])
def findCofins():
    resultado = cofinsDAO.CofinsDAO()
    return resultado.findCofins(request.json)


@app.route("/CofinsID", methods=["POST"])
def cofinsID():
    resultado = cofinsDAO.CofinsDAO()
    return resultado.cofinsID(request.json)


@app.route("/insCofins", methods=["POST"])
def insCofins():
    resultado = cofinsDAO.CofinsDAO()
    return resultado.insCofins(request.json)


@app.route("/updCofins", methods=["POST"])
def updCofins():
    resultado = cofinsDAO.CofinsDAO()
    return resultado.updCofins(request.json)


@app.route("/delCofins", methods=["POST"])
def delCofins():
    resultado = cofinsDAO.CofinsDAO()
    return resultado.delCofins(request.json)


"""
  Fim rota: Cofins
"""

"""
  Rotas do WebService para a classe: Ipi (TB01054)
"""
import ipiDAO


@app.route("/listIpi/", methods=["POST"])
def listIpi():
    resultado = ipiDAO.IpiDAO()
    return resultado.listIpi(request.json)


@app.route("/dictIpi/", methods=["POST"])
def dictIpi():
    resultado = ipiDAO.IpiDAO()
    return resultado.dictIpi(request.json)


@app.route("/fieldsIpi/", methods=["POST"])
def fieldsIpi():
    resultado = ipiDAO.IpiDAO()
    return resultado.fieldsIpi(request.json)


@app.route("/findIpi/", methods=["POST"])
def findIpi():
    resultado = ipiDAO.IpiDAO()
    return resultado.findIpi(request.json)


@app.route("/IpiID", methods=["POST"])
def ipiID():
    resultado = ipiDAO.IpiDAO()
    return resultado.ipiID(request.json)


@app.route("/insIpi", methods=["POST"])
def insIpi():
    resultado = ipiDAO.IpiDAO()
    return resultado.insIpi(request.json)


@app.route("/updIpi", methods=["POST"])
def updIpi():
    resultado = ipiDAO.IpiDAO()
    return resultado.updIpi(request.json)


@app.route("/delIpi", methods=["POST"])
def delIpi():
    resultado = ipiDAO.IpiDAO()
    return resultado.delIpi(request.json)


"""
  Fim rota: Ipi
"""

"""
  Rotas do WebService para a classe: Pis (TB01052)
"""
import pisDAO


@app.route("/listPis/", methods=["POST"])
def listPis():
    resultado = pisDAO.PisDAO()
    return resultado.listPis(request.json)


@app.route("/dictPis/", methods=["POST"])
def dictPis():
    resultado = pisDAO.PisDAO()
    return resultado.dictPis(request.json)


@app.route("/fieldsPis/", methods=["POST"])
def fieldsPis():
    resultado = pisDAO.PisDAO()
    return resultado.fieldsPis(request.json)


@app.route("/findPis/", methods=["POST"])
def findPis():
    resultado = pisDAO.PisDAO()
    return resultado.findPis(request.json)


@app.route("/PisID", methods=["POST"])
def pisID():
    resultado = pisDAO.PisDAO()
    return resultado.pisID(request.json)


@app.route("/insPis", methods=["POST"])
def insPis():
    resultado = pisDAO.PisDAO()
    return resultado.insPis(request.json)


@app.route("/updPis", methods=["POST"])
def updPis():
    resultado = pisDAO.PisDAO()
    return resultado.updPis(request.json)


@app.route("/delPis", methods=["POST"])
def delPis():
    resultado = pisDAO.PisDAO()
    return resultado.delPis(request.json)


"""
  Fim rota: Pis
"""

"""
  Rotas do WebService para a classe: Local (TB01003)
"""
import localDAO


@app.route("/listLocal/", methods=["POST"])
def listLocal():
    resultado = localDAO.LocalDAO()
    return resultado.listLocal(request.json)


@app.route("/dictLocal/", methods=["POST"])
def dictLocal():
    resultado = localDAO.LocalDAO()
    return resultado.dictLocal(request.json)


@app.route("/fieldsLocal/", methods=["POST"])
def fieldsLocal():
    resultado = localDAO.LocalDAO()
    return resultado.fieldsLocal(request.json)


@app.route("/findLocal/", methods=["POST"])
def findLocal():
    resultado = localDAO.LocalDAO()
    return resultado.findLocal(request.json)


@app.route("/LocalID", methods=["POST"])
def localID():
    resultado = localDAO.LocalDAO()
    return resultado.localID(request.json)


@app.route("/insLocal", methods=["POST"])
def insLocal():
    resultado = localDAO.LocalDAO()
    return resultado.insLocal(request.json)


@app.route("/updLocal", methods=["POST"])
def updLocal():
    resultado = localDAO.LocalDAO()
    return resultado.updLocal(request.json)


@app.route("/delLocal", methods=["POST"])
def delLocal():
    resultado = localDAO.LocalDAO()
    return resultado.delLocal(request.json)


"""
  Fim rota: Local
"""

"""
  Rotas do WebService para a classe: Marca (TB01047)
"""
import marcaDAO


@app.route("/listMarca/", methods=["POST"])
def listMarca():
    resultado = marcaDAO.MarcaDAO()
    return resultado.listMarca(request.json)


@app.route("/dictMarca/", methods=["POST"])
def dictMarca():
    resultado = marcaDAO.MarcaDAO()
    return resultado.dictMarca(request.json)


@app.route("/fieldsMarca/", methods=["POST"])
def fieldsMarca():
    resultado = marcaDAO.MarcaDAO()
    return resultado.fieldsMarca(request.json)


@app.route("/findMarca/", methods=["POST"])
def findMarca():
    resultado = marcaDAO.MarcaDAO()
    return resultado.findMarca(request.json)


@app.route("/MarcaID", methods=["POST"])
def marcaID():
    resultado = marcaDAO.MarcaDAO()
    return resultado.marcaID(request.json)


@app.route("/insMarca", methods=["POST"])
def insMarca():
    resultado = marcaDAO.MarcaDAO()
    return resultado.insMarca(request.json)


@app.route("/updMarca", methods=["POST"])
def updMarca():
    resultado = marcaDAO.MarcaDAO()
    return resultado.updMarca(request.json)


@app.route("/delMarca", methods=["POST"])
def delMarca():
    resultado = marcaDAO.MarcaDAO()
    return resultado.delMarca(request.json)


"""
  Fim rota: Marca
"""

"""
  Rotas do WebService para a classe: Icms (TB01051)
"""
import icmsDAO


@app.route("/listIcms/", methods=["POST"])
def listIcms():
    resultado = icmsDAO.IcmsDAO()
    return resultado.listIcms(request.json)


@app.route("/dictIcms/", methods=["POST"])
def dictIcms():
    resultado = icmsDAO.IcmsDAO()
    return resultado.dictIcms(request.json)


@app.route("/fieldsIcms/", methods=["POST"])
def fieldsIcms():
    resultado = icmsDAO.IcmsDAO()
    return resultado.fieldsIcms(request.json)


@app.route("/findIcms/", methods=["POST"])
def findIcms():
    resultado = icmsDAO.IcmsDAO()
    return resultado.findIcms(request.json)


@app.route("/IcmsID", methods=["POST"])
def icmsID():
    resultado = icmsDAO.IcmsDAO()
    return resultado.icmsID(request.json)


@app.route("/insIcms", methods=["POST"])
def insIcms():
    resultado = icmsDAO.IcmsDAO()
    return resultado.insIcms(request.json)


@app.route("/updIcms", methods=["POST"])
def updIcms():
    resultado = icmsDAO.IcmsDAO()
    return resultado.updIcms(request.json)


@app.route("/delIcms", methods=["POST"])
def delIcms():
    resultado = icmsDAO.IcmsDAO()
    return resultado.delIcms(request.json)


"""
  Fim rota: Icms
"""

"""
  Rotas do WebService para a classe: Unidade (TB01004)
"""
import unidadeDAO


@app.route("/listUnidade/", methods=["POST"])
def listUnidade():
    resultado = unidadeDAO.UnidadeDAO()
    return resultado.listUnidade(request.json)


@app.route("/dictUnidade/", methods=["POST"])
def dictUnidade():
    resultado = unidadeDAO.UnidadeDAO()
    return resultado.dictUnidade(request.json)


@app.route("/fieldsUnidade/", methods=["POST"])
def fieldsUnidade():
    resultado = unidadeDAO.UnidadeDAO()
    return resultado.fieldsUnidade(request.json)


@app.route("/findUnidade/", methods=["POST"])
def findUnidade():
    resultado = unidadeDAO.UnidadeDAO()
    return resultado.findUnidade(request.json)


@app.route("/UnidadeID", methods=["POST"])
def unidadeID():
    resultado = unidadeDAO.UnidadeDAO()
    return resultado.unidadeID(request.json)


@app.route("/insUnidade", methods=["POST"])
def insUnidade():
    resultado = unidadeDAO.UnidadeDAO()
    return resultado.insUnidade(request.json)


@app.route("/updUnidade", methods=["POST"])
def updUnidade():
    resultado = unidadeDAO.UnidadeDAO()
    return resultado.updUnidade(request.json)


@app.route("/delUnidade", methods=["POST"])
def delUnidade():
    resultado = unidadeDAO.UnidadeDAO()
    return resultado.delUnidade(request.json)


"""
  Fim rota: Unidade
"""

"""
  Rotas do WebService para a classe: Fornecedor (TB01001)
"""
import fornecedorDAO


@app.route("/listFornecedor/", methods=["POST"])
def listFornecedor():
    resultado = fornecedorDAO.FornecedorDAO()
    return resultado.listFornecedor(request.json)


@app.route("/dictFornecedor/", methods=["POST"])
def dictFornecedor():
    resultado = fornecedorDAO.FornecedorDAO()
    return resultado.dictFornecedor(request.json)


@app.route("/fieldsFornecedor/", methods=["POST"])
def fieldsFornecedor():
    resultado = fornecedorDAO.FornecedorDAO()
    return resultado.fieldsFornecedor(request.json)


@app.route("/findFornecedor/", methods=["POST"])
def findFornecedor():
    resultado = fornecedorDAO.FornecedorDAO()
    return resultado.findFornecedor(request.json)


@app.route("/FornecedorID", methods=["POST"])
def fornecedorID():
    resultado = fornecedorDAO.FornecedorDAO()
    return resultado.fornecedorID(request.json)


@app.route("/insFornecedor", methods=["POST"])
def insFornecedor():
    resultado = fornecedorDAO.FornecedorDAO()
    return resultado.insFornecedor(request.json)


@app.route("/updFornecedor", methods=["POST"])
def updFornecedor():
    resultado = fornecedorDAO.FornecedorDAO()
    return resultado.updFornecedor(request.json)


@app.route("/delFornecedor", methods=["POST"])
def delFornecedor():
    resultado = fornecedorDAO.FornecedorDAO()
    return resultado.delFornecedor(request.json)


"""
  Fim rota: Fornecedor
"""

"""
  Rotas do WebService para a classe: Produto (TB01010)
"""
import produtoDAO


@app.route("/listProduto/", methods=["POST"])
def listProduto():
    resultado = produtoDAO.ProdutoDAO()
    return resultado.listProduto(request.json)


@app.route("/dictProduto/", methods=["POST"])
def dictProduto():
    resultado = produtoDAO.ProdutoDAO()
    return resultado.dictProduto(request.json)


@app.route("/fieldsProduto/", methods=["POST"])
def fieldsProduto():
    resultado = produtoDAO.ProdutoDAO()
    return resultado.fieldsProduto(request.json)


@app.route("/findProduto/", methods=["POST"])
def findProduto():
    resultado = produtoDAO.ProdutoDAO()
    return resultado.findProduto(request.json)


@app.route("/ProdutoID", methods=["POST"])
def produtoID():
    resultado = produtoDAO.ProdutoDAO()
    return resultado.produtoID(request.json)


@app.route("/insProduto", methods=["POST"])
def insProduto():
    resultado = produtoDAO.ProdutoDAO()
    return resultado.insProduto(request.json)


@app.route("/updProduto", methods=["POST"])
def updProduto():
    resultado = produtoDAO.ProdutoDAO()
    return resultado.updProduto(request.json)


@app.route("/delProduto", methods=["POST"])
def delProduto():
    resultado = produtoDAO.ProdutoDAO()
    return resultado.delProduto(request.json)


"""
  Fim rota: Produto
"""

"""
  Rotas do WebService para a classe: ClasificacaoVenda (TB01068)
"""
import clasificacaovendaDAO


@app.route("/listClasificacaoVenda/", methods=["POST"])
def listClasificacaoVenda():
    resultado = clasificacaovendaDAO.ClasificacaoVendaDAO()
    return resultado.listClasificacaoVenda(request.json)


@app.route("/dictClasificacaoVenda/", methods=["POST"])
def dictClasificacaoVenda():
    resultado = clasificacaovendaDAO.ClasificacaoVendaDAO()
    return resultado.dictClasificacaoVenda(request.json)


@app.route("/fieldsClasificacaoVenda/", methods=["POST"])
def fieldsClasificacaoVenda():
    resultado = clasificacaovendaDAO.ClasificacaoVendaDAO()
    return resultado.fieldsClasificacaoVenda(request.json)


@app.route("/findClasificacaoVenda/", methods=["POST"])
def findClasificacaoVenda():
    resultado = clasificacaovendaDAO.ClasificacaoVendaDAO()
    return resultado.findClasificacaoVenda(request.json)


@app.route("/ClasificacaovendaID", methods=["POST"])
def clasificacaovendaID():
    resultado = clasificacaovendaDAO.ClasificacaoVendaDAO()
    return resultado.clasificacaovendaID(request.json)


@app.route("/insClasificacaoVenda", methods=["POST"])
def insClasificacaoVenda():
    resultado = clasificacaovendaDAO.ClasificacaoVendaDAO()
    return resultado.insClasificacaoVenda(request.json)


@app.route("/updClasificacaoVenda", methods=["POST"])
def updClasificacaoVenda():
    resultado = clasificacaovendaDAO.ClasificacaoVendaDAO()
    return resultado.updClasificacaoVenda(request.json)


@app.route("/delClasificacaoVenda", methods=["POST"])
def delClasificacaoVenda():
    resultado = clasificacaovendaDAO.ClasificacaoVendaDAO()
    return resultado.delClasificacaoVenda(request.json)


"""
  Fim rota: ClasificacaoVenda
"""

"""
  Rotas do WebService para a classe: Departamento (TB02177)
"""
import departamentoDAO


@app.route("/listDepartamento/", methods=["POST"])
def listDepartamento():
    resultado = departamentoDAO.DepartamentoDAO()
    return resultado.listDepartamento(request.json)


@app.route("/dictDepartamento/", methods=["POST"])
def dictDepartamento():
    resultado = departamentoDAO.DepartamentoDAO()
    return resultado.dictDepartamento(request.json)


@app.route("/fieldsDepartamento/", methods=["POST"])
def fieldsDepartamento():
    resultado = departamentoDAO.DepartamentoDAO()
    return resultado.fieldsDepartamento(request.json)


@app.route("/findDepartamento/", methods=["POST"])
def findDepartamento():
    resultado = departamentoDAO.DepartamentoDAO()
    return resultado.findDepartamento(request.json)


@app.route("/DepartamentoID", methods=["POST"])
def departamentoID():
    resultado = departamentoDAO.DepartamentoDAO()
    return resultado.departamentoID(request.json)


@app.route("/insDepartamento", methods=["POST"])
def insDepartamento():
    resultado = departamentoDAO.DepartamentoDAO()
    return resultado.insDepartamento(request.json)


@app.route("/updDepartamento", methods=["POST"])
def updDepartamento():
    resultado = departamentoDAO.DepartamentoDAO()
    return resultado.updDepartamento(request.json)


@app.route("/delDepartamento", methods=["POST"])
def delDepartamento():
    resultado = departamentoDAO.DepartamentoDAO()
    return resultado.delDepartamento(request.json)


"""
  Fim rota: Departamento
"""

"""
  Rotas do WebService para a classe: Site (TB02176)
"""
import siteDAO


@app.route("/listSite/", methods=["POST"])
def listSite():
    resultado = siteDAO.SiteDAO()
    return resultado.listSite(request.json)


@app.route("/dictSite/", methods=["POST"])
def dictSite():
    resultado = siteDAO.SiteDAO()
    return resultado.dictSite(request.json)


@app.route("/fieldsSite/", methods=["POST"])
def fieldsSite():
    resultado = siteDAO.SiteDAO()
    return resultado.fieldsSite(request.json)


@app.route("/findSite/", methods=["POST"])
def findSite():
    resultado = siteDAO.SiteDAO()
    return resultado.findSite(request.json)


@app.route("/SiteID", methods=["POST"])
def siteID():
    resultado = siteDAO.SiteDAO()
    return resultado.siteID(request.json)


@app.route("/insSite", methods=["POST"])
def insSite():
    resultado = siteDAO.SiteDAO()
    return resultado.insSite(request.json)


@app.route("/updSite", methods=["POST"])
def updSite():
    resultado = siteDAO.SiteDAO()
    return resultado.updSite(request.json)


@app.route("/delSite", methods=["POST"])
def delSite():
    resultado = siteDAO.SiteDAO()
    return resultado.delSite(request.json)


"""
  Fim rota: Site
"""

"""
  Rotas do WebService para a classe: Orcamento (TB02018)
"""
import orcamentoDAO


@app.route("/listOrcamento/", methods=["POST"])
def listOrcamento():
    resultado = orcamentoDAO.OrcamentoDAO()
    return resultado.listOrcamento(request.json)


@app.route("/dictOrcamento/", methods=["POST"])
def dictOrcamento():
    resultado = orcamentoDAO.OrcamentoDAO()
    return resultado.dictOrcamento(request.json)


@app.route("/fieldsOrcamento/", methods=["POST"])
def fieldsOrcamento():
    resultado = orcamentoDAO.OrcamentoDAO()
    return resultado.fieldsOrcamento(request.json)


@app.route("/findOrcamento/", methods=["POST"])
def findOrcamento():
    resultado = orcamentoDAO.OrcamentoDAO()
    return resultado.findOrcamento(request.json)


@app.route("/OrcamentoID", methods=["POST"])
def orcamentoID():
    resultado = orcamentoDAO.OrcamentoDAO()
    return resultado.orcamentoID(request.json)


@app.route("/insOrcamento", methods=["POST"])
def insOrcamento():
    resultado = orcamentoDAO.OrcamentoDAO()
    return resultado.insOrcamento(request.json)


@app.route("/updOrcamento", methods=["POST"])
def updOrcamento():
    resultado = orcamentoDAO.OrcamentoDAO()
    return resultado.updOrcamento(request.json)


@app.route("/delOrcamento", methods=["POST"])
def delOrcamento():
    resultado = orcamentoDAO.OrcamentoDAO()
    return resultado.delOrcamento(request.json)


"""
  Fim rota: Orcamento
"""

"""
  Rotas do WebService para a classe: OrcamentoItem (TB02019)
"""
import orcamentoitemDAO


@app.route("/listOrcamentoItem/", methods=["POST"])
def listOrcamentoItem():
    resultado = orcamentoitemDAO.OrcamentoItemDAO()
    return resultado.listOrcamentoItem(request.json)


@app.route("/dictOrcamentoItem/", methods=["POST"])
def dictOrcamentoItem():
    resultado = orcamentoitemDAO.OrcamentoItemDAO()
    return resultado.dictOrcamentoItem(request.json)


@app.route("/fieldsOrcamentoItem/", methods=["POST"])
def fieldsOrcamentoItem():
    resultado = orcamentoitemDAO.OrcamentoItemDAO()
    return resultado.fieldsOrcamentoItem(request.json)


@app.route("/findOrcamentoItem/", methods=["POST"])
def findOrcamentoItem():
    resultado = orcamentoitemDAO.OrcamentoItemDAO()
    return resultado.findOrcamentoItem(request.json)


@app.route("/OrcamentoitemID", methods=["POST"])
def orcamentoitemID():
    resultado = orcamentoitemDAO.OrcamentoItemDAO()
    return resultado.orcamentoitemID(request.json)


@app.route("/insOrcamentoItem", methods=["POST"])
def insOrcamentoItem():
    resultado = orcamentoitemDAO.OrcamentoItemDAO()
    return resultado.insOrcamentoItem(request.json)


@app.route("/updOrcamentoItem", methods=["POST"])
def updOrcamentoItem():
    resultado = orcamentoitemDAO.OrcamentoItemDAO()
    return resultado.updOrcamentoItem(request.json)


@app.route("/delOrcamentoItem", methods=["POST"])
def delOrcamentoItem():
    resultado = orcamentoitemDAO.OrcamentoItemDAO()
    return resultado.delOrcamentoItem(request.json)


"""
  Fim rota: OrcamentoItem
"""

"""
  Rotas do WebService para a classe: OrcamentoServico (TB02020)
"""
import orcamentoservicoDAO


@app.route("/listOrcamentoServico/", methods=["POST"])
def listOrcamentoServico():
    resultado = orcamentoservicoDAO.OrcamentoServicoDAO()
    return resultado.listOrcamentoServico(request.json)


@app.route("/dictOrcamentoServico/", methods=["POST"])
def dictOrcamentoServico():
    resultado = orcamentoservicoDAO.OrcamentoServicoDAO()
    return resultado.dictOrcamentoServico(request.json)


@app.route("/fieldsOrcamentoServico/", methods=["POST"])
def fieldsOrcamentoServico():
    resultado = orcamentoservicoDAO.OrcamentoServicoDAO()
    return resultado.fieldsOrcamentoServico(request.json)


@app.route("/findOrcamentoServico/", methods=["POST"])
def findOrcamentoServico():
    resultado = orcamentoservicoDAO.OrcamentoServicoDAO()
    return resultado.findOrcamentoServico(request.json)


@app.route("/OrcamentoservicoID", methods=["POST"])
def orcamentoservicoID():
    resultado = orcamentoservicoDAO.OrcamentoServicoDAO()
    return resultado.orcamentoservicoID(request.json)


@app.route("/insOrcamentoServico", methods=["POST"])
def insOrcamentoServico():
    resultado = orcamentoservicoDAO.OrcamentoServicoDAO()
    return resultado.insOrcamentoServico(request.json)


@app.route("/updOrcamentoServico", methods=["POST"])
def updOrcamentoServico():
    resultado = orcamentoservicoDAO.OrcamentoServicoDAO()
    return resultado.updOrcamentoServico(request.json)


@app.route("/delOrcamentoServico", methods=["POST"])
def delOrcamentoServico():
    resultado = orcamentoservicoDAO.OrcamentoServicoDAO()
    return resultado.delOrcamentoServico(request.json)


"""
  Fim rota: OrcamentoServico
"""

"""
  Rotas do WebService para a classe: OrcamentoParcela (TB02098)
"""
import orcamentoparcelaDAO


@app.route("/listOrcamentoParcela/", methods=["POST"])
def listOrcamentoParcela():
    resultado = orcamentoparcelaDAO.OrcamentoParcelaDAO()
    return resultado.listOrcamentoParcela(request.json)


@app.route("/dictOrcamentoParcela/", methods=["POST"])
def dictOrcamentoParcela():
    resultado = orcamentoparcelaDAO.OrcamentoParcelaDAO()
    return resultado.dictOrcamentoParcela(request.json)


@app.route("/fieldsOrcamentoParcela/", methods=["POST"])
def fieldsOrcamentoParcela():
    resultado = orcamentoparcelaDAO.OrcamentoParcelaDAO()
    return resultado.fieldsOrcamentoParcela(request.json)


@app.route("/findOrcamentoParcela/", methods=["POST"])
def findOrcamentoParcela():
    resultado = orcamentoparcelaDAO.OrcamentoParcelaDAO()
    return resultado.findOrcamentoParcela(request.json)


@app.route("/OrcamentoparcelaID", methods=["POST"])
def orcamentoparcelaID():
    resultado = orcamentoparcelaDAO.OrcamentoParcelaDAO()
    return resultado.orcamentoparcelaID(request.json)


@app.route("/insOrcamentoParcela", methods=["POST"])
def insOrcamentoParcela():
    resultado = orcamentoparcelaDAO.OrcamentoParcelaDAO()
    return resultado.insOrcamentoParcela(request.json)


@app.route("/updOrcamentoParcela", methods=["POST"])
def updOrcamentoParcela():
    resultado = orcamentoparcelaDAO.OrcamentoParcelaDAO()
    return resultado.updOrcamentoParcela(request.json)


@app.route("/delOrcamentoParcela", methods=["POST"])
def delOrcamentoParcela():
    resultado = orcamentoparcelaDAO.OrcamentoParcelaDAO()
    return resultado.delOrcamentoParcela(request.json)


"""
  Fim rota: OrcamentoParcela
"""

"""
  Rotas do WebService para a classe: fieldslist
"""
import fieldslist


@app.route("/fieldsList", methods=["POST"])
def fieldsList():
    resultado = fieldslist.fieldList()
    return resultado.executeList(request.json)


@app.route("/fieldsDict", methods=["POST"])
def dictList():
    resultado = fieldslist.fieldList()
    return resultado.dictList(request.json)


@app.route("/browseList", methods=["POST"])
def browseList():
    resultado = fieldslist.fieldList()
    return resultado.browseList(request.json)


"""
  Fim rota: fieldslist
"""

"""
  Rotas do WebService para a classe: EnderecoTipo (TB04002)
"""
import enderecotipoDAO


@app.route("/listEnderecoTipo/", methods=["POST"])
def listEnderecoTipo():
    resultado = enderecotipoDAO.EnderecoTipoDAO()
    return resultado.listEnderecoTipo(request.json)


@app.route("/dictEnderecoTipo/", methods=["POST"])
def dictEnderecoTipo():
    resultado = enderecotipoDAO.EnderecoTipoDAO()
    return resultado.dictEnderecoTipo(request.json)


@app.route("/fieldsEnderecoTipo/", methods=["POST"])
def fieldsEnderecoTipo():
    resultado = enderecotipoDAO.EnderecoTipoDAO()
    return resultado.fieldsEnderecoTipo(request.json)


@app.route("/findEnderecoTipo/", methods=["POST"])
def findEnderecoTipo():
    resultado = enderecotipoDAO.EnderecoTipoDAO()
    return resultado.findEnderecoTipo(request.json)


@app.route("/EnderecotipoID", methods=["POST"])
def enderecotipoID():
    resultado = enderecotipoDAO.EnderecoTipoDAO()
    return resultado.enderecotipoID(request.json)


@app.route("/insEnderecoTipo", methods=["POST"])
def insEnderecoTipo():
    resultado = enderecotipoDAO.EnderecoTipoDAO()
    return resultado.insEnderecoTipo(request.json)


@app.route("/updEnderecoTipo", methods=["POST"])
def updEnderecoTipo():
    resultado = enderecotipoDAO.EnderecoTipoDAO()
    return resultado.updEnderecoTipo(request.json)


@app.route("/delEnderecoTipo", methods=["POST"])
def delEnderecoTipo():
    resultado = enderecotipoDAO.EnderecoTipoDAO()
    return resultado.delEnderecoTipo(request.json)


"""
  Fim rota: EnderecoTipo
"""

"""
  Rotas do WebService para a classe: EnderecoConfig (TB00013)
"""
import enderecoconfigDAO


@app.route("/listEnderecoConfig/", methods=["POST"])
def listEnderecoConfig():
    resultado = enderecoconfigDAO.EnderecoConfigDAO()
    return resultado.listEnderecoConfig(request.json)


@app.route("/dictEnderecoConfig/", methods=["POST"])
def dictEnderecoConfig():
    resultado = enderecoconfigDAO.EnderecoConfigDAO()
    return resultado.dictEnderecoConfig(request.json)


@app.route("/fieldsEnderecoConfig/", methods=["POST"])
def fieldsEnderecoConfig():
    resultado = enderecoconfigDAO.EnderecoConfigDAO()
    return resultado.fieldsEnderecoConfig(request.json)


@app.route("/insEnderecoConfig", methods=["POST"])
def insEnderecoConfig():
    resultado = enderecoconfigDAO.EnderecoConfigDAO()
    return resultado.insEnderecoConfig(request.json)


@app.route("/updEnderecoConfig", methods=["POST"])
def updEnderecoConfig():
    resultado = enderecoconfigDAO.EnderecoConfigDAO()
    return resultado.updEnderecoConfig(request.json)


@app.route("/delEnderecoConfig", methods=["POST"])
def delEnderecoConfig():
    resultado = enderecoconfigDAO.EnderecoConfigDAO()
    return resultado.delEnderecoConfig(request.json)


"""
  Fim rota: EnderecoConfig
"""

"""
  Rotas do WebService para a classe: EnderecoConfigVW (VW00007)
"""
import enderecoconfigvwDAO


@app.route("/listEnderecoConfigVW/", methods=["POST"])
def listEnderecoConfigVW():
    resultado = enderecoconfigvwDAO.EnderecoConfigVWDAO()
    return resultado.listEnderecoConfigVW(request.json)


@app.route("/dictEnderecoConfigVW/", methods=["POST"])
def dictEnderecoConfigVW():
    resultado = enderecoconfigvwDAO.EnderecoConfigVWDAO()
    return resultado.dictEnderecoConfigVW(request.json)


@app.route("/fieldsEnderecoConfigVW/", methods=["POST"])
def fieldsEnderecoConfigVW():
    resultado = enderecoconfigvwDAO.EnderecoConfigVWDAO()
    return resultado.fieldsEnderecoConfigVW(request.json)


"""
  Fim rota: EnderecoConfigVW
"""

"""
  Rotas do WebService para a classe: Permissao (TB00037)
"""
import permissaoDAO


@app.route("/listPermissao/", methods=["POST"])
def listPermissao():
    resultado = permissaoDAO.PermissaoDAO()
    return resultado.listPermissao(request.json)


@app.route("/dictPermissao/", methods=["POST"])
def dictPermissao():
    resultado = permissaoDAO.PermissaoDAO()
    return resultado.dictPermissao(request.json)


@app.route("/fieldsPermissao/", methods=["POST"])
def fieldsPermissao():
    resultado = permissaoDAO.PermissaoDAO()
    return resultado.fieldsPermissao(request.json)


@app.route("/findPermissao/", methods=["POST"])
def findPermissao():
    resultado = permissaoDAO.PermissaoDAO()
    return resultado.findPermissao(request.json)


@app.route("/insPermissao", methods=["POST"])
def insPermissao():
    resultado = permissaoDAO.PermissaoDAO()
    return resultado.insPermissao(request.json)


@app.route("/updPermissao", methods=["POST"])
def updPermissao():
    resultado = permissaoDAO.PermissaoDAO()
    return resultado.updPermissao(request.json)


@app.route("/delPermissao", methods=["POST"])
def delPermissao():
    resultado = permissaoDAO.PermissaoDAO()
    return resultado.delPermissao(request.json)


"""
  Fim rota: Permissao
"""

"""
  Rotas do WebService para a classe: Fieldlist (TB00101)
"""
import fieldlistDAO


@app.route("/listFieldlist/", methods=["POST"])
def listFieldlist():
    resultado = fieldlistDAO.FieldlistDAO()
    return resultado.listFieldlist(request.json)


@app.route("/dictFieldlist/", methods=["POST"])
def dictFieldlist():
    resultado = fieldlistDAO.FieldlistDAO()
    return resultado.dictFieldlist(request.json)


@app.route("/fieldsFieldlist/", methods=["POST"])
def fieldsFieldlist():
    resultado = fieldlistDAO.FieldlistDAO()
    return resultado.fieldsFieldlist(request.json)


@app.route("/findFieldlist/", methods=["POST"])
def findFieldlist():
    resultado = fieldlistDAO.FieldlistDAO()
    return resultado.findFieldlist(request.json)


@app.route("/insFieldlist", methods=["POST"])
def insFieldlist():
    resultado = fieldlistDAO.FieldlistDAO()
    return resultado.insFieldlist(request.json)


@app.route("/updFieldlist", methods=["POST"])
def updFieldlist():
    resultado = fieldlistDAO.FieldlistDAO()
    return resultado.updFieldlist(request.json)


@app.route("/delFieldlist", methods=["POST"])
def delFieldlist():
    resultado = fieldlistDAO.FieldlistDAO()
    return resultado.delFieldlist(request.json)


"""
  Fim rota: Fieldlist
"""

"""
  Rotas do WebService para a classe: Fieldfilter (TB00102)
"""
import fieldfilterDAO


@app.route("/listFieldfilter/", methods=["POST"])
def listFieldfilter():
    resultado = fieldfilterDAO.FieldfilterDAO()
    return resultado.listFieldfilter(request.json)


@app.route("/dictFieldfilter/", methods=["POST"])
def dictFieldfilter():
    resultado = fieldfilterDAO.FieldfilterDAO()
    return resultado.dictFieldfilter(request.json)


@app.route("/fieldsFieldfilter/", methods=["POST"])
def fieldsFieldfilter():
    resultado = fieldfilterDAO.FieldfilterDAO()
    return resultado.fieldsFieldfilter(request.json)


@app.route("/findFieldfilter/", methods=["POST"])
def findFieldfilter():
    resultado = fieldfilterDAO.FieldfilterDAO()
    return resultado.findFieldfilter(request.json)


@app.route("/insFieldfilter", methods=["POST"])
def insFieldfilter():
    resultado = fieldfilterDAO.FieldfilterDAO()
    return resultado.insFieldfilter(request.json)


@app.route("/updFieldfilter", methods=["POST"])
def updFieldfilter():
    resultado = fieldfilterDAO.FieldfilterDAO()
    return resultado.updFieldfilter(request.json)


@app.route("/delFieldfilter", methods=["POST"])
def delFieldfilter():
    resultado = fieldfilterDAO.FieldfilterDAO()
    return resultado.delFieldfilter(request.json)


"""
  Fim rota: Fieldfilter
"""

"""
  Rotas do WebService para a classe: Optionlist (TB00103)
"""
import optionlistDAO


@app.route("/listOptionlist/", methods=["POST"])
def listOptionlist():
    resultado = optionlistDAO.OptionlistDAO()
    return resultado.listOptionlist(request.json)


@app.route("/dictOptionlist/", methods=["POST"])
def dictOptionlist():
    resultado = optionlistDAO.OptionlistDAO()
    return resultado.dictOptionlist(request.json)


@app.route("/fieldsOptionlist/", methods=["POST"])
def fieldsOptionlist():
    resultado = optionlistDAO.OptionlistDAO()
    return resultado.fieldsOptionlist(request.json)


@app.route("/findOptionlist/", methods=["POST"])
def findOptionlist():
    resultado = optionlistDAO.OptionlistDAO()
    return resultado.findOptionlist(request.json)


@app.route("/OptionlistID", methods=["POST"])
def optionlistID():
    resultado = optionlistDAO.OptionlistDAO()
    return resultado.optionlistID(request.json)


@app.route("/insOptionlist", methods=["POST"])
def insOptionlist():
    resultado = optionlistDAO.OptionlistDAO()
    return resultado.insOptionlist(request.json)


@app.route("/updOptionlist", methods=["POST"])
def updOptionlist():
    resultado = optionlistDAO.OptionlistDAO()
    return resultado.updOptionlist(request.json)


@app.route("/delOptionlist", methods=["POST"])
def delOptionlist():
    resultado = optionlistDAO.OptionlistDAO()
    return resultado.delOptionlist(request.json)


"""
  Fim rota: Optionlist
"""

"""
  Rotas do WebService para a classe: Optionfilter (TB00105)
"""
import optionfilterDAO


@app.route("/listOptionfilter/", methods=["POST"])
def listOptionfilter():
    resultado = optionfilterDAO.OptionfilterDAO()
    return resultado.listOptionfilter(request.json)


@app.route("/dictOptionfilter/", methods=["POST"])
def dictOptionfilter():
    resultado = optionfilterDAO.OptionfilterDAO()
    return resultado.dictOptionfilter(request.json)


@app.route("/fieldsOptionfilter/", methods=["POST"])
def fieldsOptionfilter():
    resultado = optionfilterDAO.OptionfilterDAO()
    return resultado.fieldsOptionfilter(request.json)


@app.route("/findOptionfilter/", methods=["POST"])
def findOptionfilter():
    resultado = optionfilterDAO.OptionfilterDAO()
    return resultado.findOptionfilter(request.json)


@app.route("/OptionfilterID", methods=["POST"])
def optionfilterID():
    resultado = optionfilterDAO.OptionfilterDAO()
    return resultado.optionfilterID(request.json)


@app.route("/insOptionfilter", methods=["POST"])
def insOptionfilter():
    resultado = optionfilterDAO.OptionfilterDAO()
    return resultado.insOptionfilter(request.json)


@app.route("/updOptionfilter", methods=["POST"])
def updOptionfilter():
    resultado = optionfilterDAO.OptionfilterDAO()
    return resultado.updOptionfilter(request.json)


@app.route("/delOptionfilter", methods=["POST"])
def delOptionfilter():
    resultado = optionfilterDAO.OptionfilterDAO()
    return resultado.delOptionfilter(request.json)


"""
  Fim rota: Optionfilter
"""

"""
  Rotas do WebService para a classe: OptionlistField (TB00104)
"""
import optionlistfieldDAO


@app.route("/listOptionlistField/", methods=["POST"])
def listOptionlistField():
    resultado = optionlistfieldDAO.OptionlistFieldDAO()
    return resultado.listOptionlistField(request.json)


@app.route("/dictOptionlistField/", methods=["POST"])
def dictOptionlistField():
    resultado = optionlistfieldDAO.OptionlistFieldDAO()
    return resultado.dictOptionlistField(request.json)


@app.route("/fieldsOptionlistField/", methods=["POST"])
def fieldsOptionlistField():
    resultado = optionlistfieldDAO.OptionlistFieldDAO()
    return resultado.fieldsOptionlistField(request.json)


@app.route("/findOptionlistField/", methods=["POST"])
def findOptionlistField():
    resultado = optionlistfieldDAO.OptionlistFieldDAO()
    return resultado.findOptionlistField(request.json)


@app.route("/insOptionlistField", methods=["POST"])
def insOptionlistField():
    resultado = optionlistfieldDAO.OptionlistFieldDAO()
    return resultado.insOptionlistField(request.json)


@app.route("/updOptionlistField", methods=["POST"])
def updOptionlistField():
    resultado = optionlistfieldDAO.OptionlistFieldDAO()
    return resultado.updOptionlistField(request.json)


@app.route("/delOptionlistField", methods=["POST"])
def delOptionlistField():
    resultado = optionlistfieldDAO.OptionlistFieldDAO()
    return resultado.delOptionlistField(request.json)


"""
  Fim rota: OptionlistField
"""

"""
  Rotas do WebService para a classe: OptionfilterField (TB00106)
"""
import optionfilterfieldDAO


@app.route("/listOptionfilterField/", methods=["POST"])
def listOptionfilterField():
    resultado = optionfilterfieldDAO.OptionfilterFieldDAO()
    return resultado.listOptionfilterField(request.json)


@app.route("/dictOptionfilterField/", methods=["POST"])
def dictOptionfilterField():
    resultado = optionfilterfieldDAO.OptionfilterFieldDAO()
    return resultado.dictOptionfilterField(request.json)


@app.route("/fieldsOptionfilterField/", methods=["POST"])
def fieldsOptionfilterField():
    resultado = optionfilterfieldDAO.OptionfilterFieldDAO()
    return resultado.fieldsOptionfilterField(request.json)


@app.route("/findOptionfilterField/", methods=["POST"])
def findOptionfilterField():
    resultado = optionfilterfieldDAO.OptionfilterFieldDAO()
    return resultado.findOptionfilterField(request.json)


@app.route("/insOptionfilterField", methods=["POST"])
def insOptionfilterField():
    resultado = optionfilterfieldDAO.OptionfilterFieldDAO()
    return resultado.insOptionfilterField(request.json)


@app.route("/updOptionfilterField", methods=["POST"])
def updOptionfilterField():
    resultado = optionfilterfieldDAO.OptionfilterFieldDAO()
    return resultado.updOptionfilterField(request.json)


@app.route("/delOptionfilterField", methods=["POST"])
def delOptionfilterField():
    resultado = optionfilterfieldDAO.OptionfilterFieldDAO()
    return resultado.delOptionfilterField(request.json)


"""
  Fim rota: OptionfilterField
  
"""
app.route("/")


def hello_world():
    return "<p>Ola</p>"


"""
  Rotas do WebService para a classe: GroupForm (TB00107)
"""
import groupformDAO


@app.route("/listGroupForm/", methods=["POST"])
def listGroupForm():
    resultado = groupformDAO.GroupFormDAO()
    return resultado.listGroupForm(request.json)


@app.route("/dictGroupForm/", methods=["POST"])
def dictGroupForm():
    resultado = groupformDAO.GroupFormDAO()
    return resultado.dictGroupForm(request.json)


@app.route("/fieldsGroupForm/", methods=["POST"])
def fieldsGroupForm():
    resultado = groupformDAO.GroupFormDAO()
    return resultado.fieldsGroupForm(request.json)


@app.route("/findGroupForm/", methods=["POST"])
def findGroupForm():
    resultado = groupformDAO.GroupFormDAO()
    return resultado.findGroupForm(request.json)


@app.route("/GroupFormID", methods=["POST"])
def groupformID():
    resultado = groupformDAO.GroupFormDAO()
    return resultado.groupformID(request.json)


@app.route("/insGroupForm", methods=["POST"])
def insGroupForm():
    resultado = groupformDAO.GroupFormDAO()
    return resultado.insGroupForm(request.json)


@app.route("/updGroupForm", methods=["POST"])
def updGroupForm():
    resultado = groupformDAO.GroupFormDAO()
    return resultado.updGroupForm(request.json)


@app.route("/delGroupForm", methods=["POST"])
def delGroupForm():
    resultado = groupformDAO.GroupFormDAO()
    return resultado.delGroupForm(request.json)


"""
  Fim rota: GroupForm
"""

"""
  Rotas do WebService para a classe: Form (TB00108)
"""
import formDAO


@app.route("/listForm/", methods=["POST"])
def listForm():
    resultado = formDAO.FormDAO()
    return resultado.listForm(request.json)


@app.route("/dictForm/", methods=["POST"])
def dictForm():
    resultado = formDAO.FormDAO()
    return resultado.dictForm(request.json)


@app.route("/fieldsForm/", methods=["POST"])
def fieldsForm():
    resultado = formDAO.FormDAO()
    return resultado.fieldsForm(request.json)


@app.route("/findForm/", methods=["POST"])
def findForm():
    resultado = formDAO.FormDAO()
    return resultado.findForm(request.json)


@app.route("/FormID", methods=["POST"])
def formID():
    resultado = formDAO.FormDAO()
    return resultado.formID(request.json)


@app.route("/insForm", methods=["POST"])
def insForm():
    resultado = formDAO.FormDAO()
    return resultado.insForm(request.json)


@app.route("/updForm", methods=["POST"])
def updForm():
    resultado = formDAO.FormDAO()
    return resultado.updForm(request.json)


@app.route("/delForm", methods=["POST"])
def delForm():
    resultado = formDAO.FormDAO()
    return resultado.delForm(request.json)


"""
  Fim rota: Form
"""

"""
  Rotas do WebService para a classe: FormVW (VW00016)
"""
import formvwDAO


@app.route("/listFormVW/", methods=["POST"])
def listFormVW():
    resultado = formvwDAO.FormVWDAO()
    return resultado.listFormVW(request.json)


@app.route("/dictFormVW/", methods=["POST"])
def dictFormVW():
    resultado = formvwDAO.FormVWDAO()
    return resultado.dictFormVW(request.json)


@app.route("/fieldsFormVW/", methods=["POST"])
def fieldsFormVW():
    resultado = formvwDAO.FormVWDAO()
    return resultado.fieldsFormVW(request.json)


"""
  Fim rota: FormVW
"""

"""
  Rotas do WebService para a classe: FieldForm (TB00109)
"""
import fieldformDAO


@app.route("/listFieldForm/", methods=["POST"])
def listFieldForm():
    resultado = fieldformDAO.FieldFormDAO()
    return resultado.listFieldForm(request.json)


@app.route("/dictFieldForm/", methods=["POST"])
def dictFieldForm():
    resultado = fieldformDAO.FieldFormDAO()
    return resultado.dictFieldForm(request.json)


@app.route("/fieldsFieldForm/", methods=["POST"])
def fieldsFieldForm():
    resultado = fieldformDAO.FieldFormDAO()
    return resultado.fieldsFieldForm(request.json)


@app.route("/findFieldForm/", methods=["POST"])
def findFieldForm():
    resultado = fieldformDAO.FieldFormDAO()
    return resultado.findFieldForm(request.json)


@app.route("/insFieldForm", methods=["POST"])
def insFieldForm():
    resultado = fieldformDAO.FieldFormDAO()
    return resultado.insFieldForm(request.json)


@app.route("/updFieldForm", methods=["POST"])
def updFieldForm():
    resultado = fieldformDAO.FieldFormDAO()
    return resultado.updFieldForm(request.json)


@app.route("/delFieldForm", methods=["POST"])
def delFieldForm():
    resultado = fieldformDAO.FieldFormDAO()
    return resultado.delFieldForm(request.json)


"""
  Fim rota: FieldForm
"""

"""
  Rotas do WebService para a classe: CreateField (TB00109)
"""
import createfield


@app.route("/createField", methods=["POST"])
def createField():
    resultado = createfield.CreateField()
    return resultado.createField(request.json)


@app.route("/updateField", methods=["POST"])
def updateField():
    resultado = createfield.CreateField()
    return resultado.updateField(request.json)


@app.route("/createView", methods=["POST"])
def createView():
    resultado = createfield.CreateField()
    return resultado.createView(request.json)


"""
  Rotas do WebService para a classe: FieldFormVW (VW00017)
"""
import fieldformvwDAO


@app.route("/listFieldFormVW/", methods=["POST"])
def listFieldFormVW():
    resultado = fieldformvwDAO.FieldFormVWDAO()
    return resultado.listFieldFormVW(request.json)


@app.route("/dictFieldFormVW/", methods=["POST"])
def dictFieldFormVW():
    resultado = fieldformvwDAO.FieldFormVWDAO()
    return resultado.dictFieldFormVW(request.json)


@app.route("/fieldsFieldFormVW/", methods=["POST"])
def fieldsFieldFormVW():
    resultado = fieldformvwDAO.FieldFormVWDAO()
    return resultado.fieldsFieldFormVW(request.json)


@app.route("/findFieldFormVW/", methods=["POST"])
def findFieldFormVW():
    resultado = fieldformvwDAO.FieldFormVWDAO()
    return resultado.findFieldFormVW(request.json)


"""
  Fim rota: FieldFormVW
"""

"""
  Rotas do WebService para a classe: ContatoVW (VW01125)
"""
import contatovwDAO


@app.route("/listContatoVW/", methods=["POST"])
def listContatoVW():
    resultado = contatovwDAO.ContatoVWDAO()
    return resultado.listContatoVW(request.json)


@app.route("/dictContatoVW/", methods=["POST"])
def dictContatoVW():
    resultado = contatovwDAO.ContatoVWDAO()
    return resultado.dictContatoVW(request.json)


@app.route("/fieldsContatoVW/", methods=["POST"])
def fieldsContatoVW():
    resultado = contatovwDAO.ContatoVWDAO()
    return resultado.fieldsContatoVW(request.json)


@app.route("/findContatoVW/", methods=["POST"])
def findContatoVW():
    resultado = contatovwDAO.ContatoVWDAO()
    return resultado.findContatoVW(request.json)


@app.route("/contatovwID", methods=["POST"])
def contatovwID():
    resultado = contatovwDAO.ContatoVWDAO()
    return resultado.contatovwID(request.json)


"""
  Fim rota: ContatoVW
"""

"""
  Rotas do WebService para a classe: OportunidadeStatus (TB01129)
"""
import oportunidadestatusDAO


@app.route("/listOportunidadeStatus/", methods=["POST"])
def listOportunidadeStatus():
    resultado = oportunidadestatusDAO.OportunidadeStatusDAO()
    return resultado.listOportunidadeStatus(request.json)


@app.route("/dictOportunidadeStatus/", methods=["POST"])
def dictOportunidadeStatus():
    resultado = oportunidadestatusDAO.OportunidadeStatusDAO()
    return resultado.dictOportunidadeStatus(request.json)


@app.route("/fieldsOportunidadeStatus/", methods=["POST"])
def fieldsOportunidadeStatus():
    resultado = oportunidadestatusDAO.OportunidadeStatusDAO()
    return resultado.fieldsOportunidadeStatus(request.json)


@app.route("/findOportunidadeStatus/", methods=["POST"])
def findOportunidadeStatus():
    resultado = oportunidadestatusDAO.OportunidadeStatusDAO()
    return resultado.findOportunidadeStatus(request.json)


@app.route("/OportunidadeStatusID", methods=["POST"])
def oportunidadestatusID():
    resultado = oportunidadestatusDAO.OportunidadeStatusDAO()
    return resultado.oportunidadestatusID(request.json)


@app.route("/insOportunidadeStatus", methods=["POST"])
def insOportunidadeStatus():
    resultado = oportunidadestatusDAO.OportunidadeStatusDAO()
    return resultado.insOportunidadeStatus(request.json)


@app.route("/updOportunidadeStatus", methods=["POST"])
def updOportunidadeStatus():
    resultado = oportunidadestatusDAO.OportunidadeStatusDAO()
    return resultado.updOportunidadeStatus(request.json)


@app.route("/delOportunidadeStatus", methods=["POST"])
def delOportunidadeStatus():
    resultado = oportunidadestatusDAO.OportunidadeStatusDAO()
    return resultado.delOportunidadeStatus(request.json)


"""
  Fim rota: OportunidadeStatus
"""

"""
  Rotas do WebService para a classe: OportunidadeWorkflow (TB01130)
"""
import oportunidadeworkflowDAO


@app.route("/listOportunidadeWorkflow/", methods=["POST"])
def listOportunidadeWorkflow():
    resultado = oportunidadeworkflowDAO.OportunidadeWorkflowDAO()
    return resultado.listOportunidadeWorkflow(request.json)


@app.route("/dictOportunidadeWorkflow/", methods=["POST"])
def dictOportunidadeWorkflow():
    resultado = oportunidadeworkflowDAO.OportunidadeWorkflowDAO()
    return resultado.dictOportunidadeWorkflow(request.json)


@app.route("/fieldsOportunidadeWorkflow/", methods=["POST"])
def fieldsOportunidadeWorkflow():
    resultado = oportunidadeworkflowDAO.OportunidadeWorkflowDAO()
    return resultado.fieldsOportunidadeWorkflow(request.json)


@app.route("/findOportunidadeWorkflow/", methods=["POST"])
def findOportunidadeWorkflow():
    resultado = oportunidadeworkflowDAO.OportunidadeWorkflowDAO()
    return resultado.findOportunidadeWorkflow(request.json)


@app.route("/insOportunidadeWorkflow", methods=["POST"])
def insOportunidadeWorkflow():
    resultado = oportunidadeworkflowDAO.OportunidadeWorkflowDAO()
    return resultado.insOportunidadeWorkflow(request.json)


@app.route("/updOportunidadeWorkflow", methods=["POST"])
def updOportunidadeWorkflow():
    resultado = oportunidadeworkflowDAO.OportunidadeWorkflowDAO()
    return resultado.updOportunidadeWorkflow(request.json)


@app.route("/delOportunidadeWorkflow", methods=["POST"])
def delOportunidadeWorkflow():
    resultado = oportunidadeworkflowDAO.OportunidadeWorkflowDAO()
    return resultado.delOportunidadeWorkflow(request.json)


"""
  Fim rota: OportunidadeWorkflow
"""

"""
  Rotas do WebService para a classe: OportunidadeWorkflowVW (VW01126)
"""
import oportunidadeworkflowvwDAO


@app.route("/listOportunidadeWorkflowVW/", methods=["POST"])
def listOportunidadeWorkflowVW():
    resultado = oportunidadeworkflowvwDAO.OportunidadeWorkflowVWDAO()
    return resultado.listOportunidadeWorkflowVW(request.json)


@app.route("/dictOportunidadeWorkflowVW/", methods=["POST"])
def dictOportunidadeWorkflowVW():
    resultado = oportunidadeworkflowvwDAO.OportunidadeWorkflowVWDAO()
    return resultado.dictOportunidadeWorkflowVW(request.json)


@app.route("/fieldsOportunidadeWorkflowVW/", methods=["POST"])
def fieldsOportunidadeWorkflowVW():
    resultado = oportunidadeworkflowvwDAO.OportunidadeWorkflowVWDAO()
    return resultado.fieldsOportunidadeWorkflowVW(request.json)


@app.route("/findOportunidadeWorkflowVW/", methods=["POST"])
def findOportunidadeWorkflowVW():
    resultado = oportunidadeworkflowvwDAO.OportunidadeWorkflowVWDAO()
    return resultado.findOportunidadeWorkflowVW(request.json)


"""
  Fim rota: OportunidadeWorkflowVW
"""

"""
  Rotas do WebService para a classe: OportunidadeUser (TB01131)
"""
import oportunidadeuserDAO


@app.route("/listOportunidadeUser/", methods=["POST"])
def listOportunidadeUser():
    resultado = oportunidadeuserDAO.OportunidadeUserDAO()
    return resultado.listOportunidadeUser(request.json)


@app.route("/dictOportunidadeUser/", methods=["POST"])
def dictOportunidadeUser():
    resultado = oportunidadeuserDAO.OportunidadeUserDAO()
    return resultado.dictOportunidadeUser(request.json)


@app.route("/fieldsOportunidadeUser/", methods=["POST"])
def fieldsOportunidadeUser():
    resultado = oportunidadeuserDAO.OportunidadeUserDAO()
    return resultado.fieldsOportunidadeUser(request.json)


@app.route("/findOportunidadeUser/", methods=["POST"])
def findOportunidadeUser():
    resultado = oportunidadeuserDAO.OportunidadeUserDAO()
    return resultado.findOportunidadeUser(request.json)


@app.route("/insOportunidadeUser", methods=["POST"])
def insOportunidadeUser():
    resultado = oportunidadeuserDAO.OportunidadeUserDAO()
    return resultado.insOportunidadeUser(request.json)


@app.route("/updOportunidadeUser", methods=["POST"])
def updOportunidadeUser():
    resultado = oportunidadeuserDAO.OportunidadeUserDAO()
    return resultado.updOportunidadeUser(request.json)


@app.route("/delOportunidadeUser", methods=["POST"])
def delOportunidadeUser():
    resultado = oportunidadeuserDAO.OportunidadeUserDAO()
    return resultado.delOportunidadeUser(request.json)


"""
  Fim rota: OportunidadeUser
"""

"""
  Rotas do WebService para a classe: OportunidadeTipo (TB01132)
"""
import oportunidadetipoDAO


@app.route("/listOportunidadeTipo/", methods=["POST"])
def listOportunidadeTipo():
    resultado = oportunidadetipoDAO.OportunidadeTipoDAO()
    return resultado.listOportunidadeTipo(request.json)


@app.route("/dictOportunidadeTipo/", methods=["POST"])
def dictOportunidadeTipo():
    resultado = oportunidadetipoDAO.OportunidadeTipoDAO()
    return resultado.dictOportunidadeTipo(request.json)


@app.route("/fieldsOportunidadeTipo/", methods=["POST"])
def fieldsOportunidadeTipo():
    resultado = oportunidadetipoDAO.OportunidadeTipoDAO()
    return resultado.fieldsOportunidadeTipo(request.json)


@app.route("/findOportunidadeTipo/", methods=["POST"])
def findOportunidadeTipo():
    resultado = oportunidadetipoDAO.OportunidadeTipoDAO()
    return resultado.findOportunidadeTipo(request.json)


@app.route("/OportunidadeTipoID", methods=["POST"])
def oportunidadetipoID():
    resultado = oportunidadetipoDAO.OportunidadeTipoDAO()
    return resultado.oportunidadetipoID(request.json)


@app.route("/insOportunidadeTipo", methods=["POST"])
def insOportunidadeTipo():
    resultado = oportunidadetipoDAO.OportunidadeTipoDAO()
    return resultado.insOportunidadeTipo(request.json)


@app.route("/updOportunidadeTipo", methods=["POST"])
def updOportunidadeTipo():
    resultado = oportunidadetipoDAO.OportunidadeTipoDAO()
    return resultado.updOportunidadeTipo(request.json)


@app.route("/delOportunidadeTipo", methods=["POST"])
def delOportunidadeTipo():
    resultado = oportunidadetipoDAO.OportunidadeTipoDAO()
    return resultado.delOportunidadeTipo(request.json)


"""
  Fim rota: OportunidadeTipo
"""

"""
  Rotas do WebService para a classe: OportunidadeTipoVW (VW01127)
"""
import oportunidadetipovwDAO


@app.route("/listOportunidadeTipoVW/", methods=["POST"])
def listOportunidadeTipoVW():
    resultado = oportunidadetipovwDAO.OportunidadeTipoVWDAO()
    return resultado.listOportunidadeTipoVW(request.json)


@app.route("/dictOportunidadeTipoVW/", methods=["POST"])
def dictOportunidadeTipoVW():
    resultado = oportunidadetipovwDAO.OportunidadeTipoVWDAO()
    return resultado.dictOportunidadeTipoVW(request.json)


@app.route("/fieldsOportunidadeTipoVW/", methods=["POST"])
def fieldsOportunidadeTipoVW():
    resultado = oportunidadetipovwDAO.OportunidadeTipoVWDAO()
    return resultado.fieldsOportunidadeTipoVW(request.json)


@app.route("/findOportunidadeTipoVW/", methods=["POST"])
def findOportunidadeTipoVW():
    resultado = oportunidadetipovwDAO.OportunidadeTipoVWDAO()
    return resultado.findOportunidadeTipoVW(request.json)


@app.route("/updOportunidadeTipoVW", methods=["POST"])
def updOportunidadeTipoVW():
    resultado = oportunidadetipovwDAO.OportunidadeTipoVWDAO()
    return resultado.updOportunidadeTipoVW(request.json)


"""
  Fim rota: OportunidadeTipoVW
"""

"""
  Rotas do WebService para a classe: OportunidadeClassificacao (TB01133)
"""
import oportunidadeclassificacaoDAO


@app.route("/listOportunidadeClassificacao/", methods=["POST"])
def listOportunidadeClassificacao():
    resultado = oportunidadeclassificacaoDAO.OportunidadeClassificacaoDAO()
    return resultado.listOportunidadeClassificacao(request.json)


@app.route("/dictOportunidadeClassificacao/", methods=["POST"])
def dictOportunidadeClassificacao():
    resultado = oportunidadeclassificacaoDAO.OportunidadeClassificacaoDAO()
    return resultado.dictOportunidadeClassificacao(request.json)


@app.route("/fieldsOportunidadeClassificacao/", methods=["POST"])
def fieldsOportunidadeClassificacao():
    resultado = oportunidadeclassificacaoDAO.OportunidadeClassificacaoDAO()
    return resultado.fieldsOportunidadeClassificacao(request.json)


@app.route("/findOportunidadeClassificacao/", methods=["POST"])
def findOportunidadeClassificacao():
    resultado = oportunidadeclassificacaoDAO.OportunidadeClassificacaoDAO()
    return resultado.findOportunidadeClassificacao(request.json)


@app.route("/OportunidadeClassificacaoID", methods=["POST"])
def oportunidadeclassificacaoID():
    resultado = oportunidadeclassificacaoDAO.OportunidadeClassificacaoDAO()
    return resultado.oportunidadeclassificacaoID(request.json)


@app.route("/insOportunidadeClassificacao", methods=["POST"])
def insOportunidadeClassificacao():
    resultado = oportunidadeclassificacaoDAO.OportunidadeClassificacaoDAO()
    return resultado.insOportunidadeClassificacao(request.json)


@app.route("/updOportunidadeClassificacao", methods=["POST"])
def updOportunidadeClassificacao():
    resultado = oportunidadeclassificacaoDAO.OportunidadeClassificacaoDAO()
    return resultado.updOportunidadeClassificacao(request.json)


@app.route("/delOportunidadeClassificacao", methods=["POST"])
def delOportunidadeClassificacao():
    resultado = oportunidadeclassificacaoDAO.OportunidadeClassificacaoDAO()
    return resultado.delOportunidadeClassificacao(request.json)


"""
  Fim rota: OportunidadeClassificacao
"""

"""
  Rotas do WebService para a classe: OportunidadeProduto (TB01134)
"""
import oportunidadeprodutoDAO


@app.route("/listOportunidadeProduto/", methods=["POST"])
def listOportunidadeProduto():
    resultado = oportunidadeprodutoDAO.OportunidadeProdutoDAO()
    return resultado.listOportunidadeProduto(request.json)


@app.route("/dictOportunidadeProduto/", methods=["POST"])
def dictOportunidadeProduto():
    resultado = oportunidadeprodutoDAO.OportunidadeProdutoDAO()
    return resultado.dictOportunidadeProduto(request.json)


@app.route("/fieldsOportunidadeProduto/", methods=["POST"])
def fieldsOportunidadeProduto():
    resultado = oportunidadeprodutoDAO.OportunidadeProdutoDAO()
    return resultado.fieldsOportunidadeProduto(request.json)


@app.route("/findOportunidadeProduto/", methods=["POST"])
def findOportunidadeProduto():
    resultado = oportunidadeprodutoDAO.OportunidadeProdutoDAO()
    return resultado.findOportunidadeProduto(request.json)


@app.route("/OportunidadeProdutoID", methods=["POST"])
def oportunidadeprodutoID():
    resultado = oportunidadeprodutoDAO.OportunidadeProdutoDAO()
    return resultado.oportunidadeprodutoID(request.json)


@app.route("/insOportunidadeProduto", methods=["POST"])
def insOportunidadeProduto():
    resultado = oportunidadeprodutoDAO.OportunidadeProdutoDAO()
    return resultado.insOportunidadeProduto(request.json)


@app.route("/updOportunidadeProduto", methods=["POST"])
def updOportunidadeProduto():
    resultado = oportunidadeprodutoDAO.OportunidadeProdutoDAO()
    return resultado.updOportunidadeProduto(request.json)


@app.route("/delOportunidadeProduto", methods=["POST"])
def delOportunidadeProduto():
    resultado = oportunidadeprodutoDAO.OportunidadeProdutoDAO()
    return resultado.delOportunidadeProduto(request.json)


"""
  Fim rota: OportunidadeProduto
"""

"""
  Rotas do WebService para a classe: OportunidadeServico (TB01135)
"""
import oportunidadeservicoDAO


@app.route("/listOportunidadeServico/", methods=["POST"])
def listOportunidadeServico():
    resultado = oportunidadeservicoDAO.OportunidadeServicoDAO()
    return resultado.listOportunidadeServico(request.json)


@app.route("/dictOportunidadeServico/", methods=["POST"])
def dictOportunidadeServico():
    resultado = oportunidadeservicoDAO.OportunidadeServicoDAO()
    return resultado.dictOportunidadeServico(request.json)


@app.route("/fieldsOportunidadeServico/", methods=["POST"])
def fieldsOportunidadeServico():
    resultado = oportunidadeservicoDAO.OportunidadeServicoDAO()
    return resultado.fieldsOportunidadeServico(request.json)


@app.route("/findOportunidadeServico/", methods=["POST"])
def findOportunidadeServico():
    resultado = oportunidadeservicoDAO.OportunidadeServicoDAO()
    return resultado.findOportunidadeServico(request.json)


@app.route("/OportunidadeServicoID", methods=["POST"])
def oportunidadeservicoID():
    resultado = oportunidadeservicoDAO.OportunidadeServicoDAO()
    return resultado.oportunidadeservicoID(request.json)


@app.route("/insOportunidadeServico", methods=["POST"])
def insOportunidadeServico():
    resultado = oportunidadeservicoDAO.OportunidadeServicoDAO()
    return resultado.insOportunidadeServico(request.json)


@app.route("/updOportunidadeServico", methods=["POST"])
def updOportunidadeServico():
    resultado = oportunidadeservicoDAO.OportunidadeServicoDAO()
    return resultado.updOportunidadeServico(request.json)


@app.route("/delOportunidadeServico", methods=["POST"])
def delOportunidadeServico():
    resultado = oportunidadeservicoDAO.OportunidadeServicoDAO()
    return resultado.delOportunidadeServico(request.json)


"""
  Fim rota: OportunidadeServico
"""

"""
  Rotas do WebService para a classe: Oportunidade (TB02255)
"""
import oportunidadeDAO


@app.route("/listOportunidade/", methods=["POST"])
def listOportunidade():
    resultado = oportunidadeDAO.OportunidadeDAO()
    return resultado.listOportunidade(request.json)


@app.route("/dictOportunidade/", methods=["POST"])
def dictOportunidade():
    resultado = oportunidadeDAO.OportunidadeDAO()
    return resultado.dictOportunidade(request.json)


@app.route("/fieldsOportunidade/", methods=["POST"])
def fieldsOportunidade():
    resultado = oportunidadeDAO.OportunidadeDAO()
    return resultado.fieldsOportunidade(request.json)


@app.route("/findOportunidade/", methods=["POST"])
def findOportunidade():
    resultado = oportunidadeDAO.OportunidadeDAO()
    return resultado.findOportunidade(request.json)


@app.route("/OportunidadeID", methods=["POST"])
def oportunidadeID():
    resultado = oportunidadeDAO.OportunidadeDAO()
    return resultado.oportunidadeID(request.json)


@app.route("/insOportunidade", methods=["POST"])
def insOportunidade():
    resultado = oportunidadeDAO.OportunidadeDAO()
    return resultado.insOportunidade(request.json)


@app.route("/updOportunidade", methods=["POST"])
def updOportunidade():
    resultado = oportunidadeDAO.OportunidadeDAO()
    return resultado.updOportunidade(request.json)


@app.route("/delOportunidade", methods=["POST"])
def delOportunidade():
    resultado = oportunidadeDAO.OportunidadeDAO()
    return resultado.delOportunidade(request.json)


"""
  Fim rota: Oportunidade
"""

"""
  Rotas do WebService para a classe: OportunidadeVW (VW02273)
"""
import oportunidadevwDAO


@app.route("/listOportunidadeVW/", methods=["POST"])
def listOportunidadeVW():
    resultado = oportunidadevwDAO.OportunidadeVWDAO()
    return resultado.listOportunidadeVW(request.json)


@app.route("/dictOportunidadeVW/", methods=["POST"])
def dictOportunidadeVW():
    resultado = oportunidadevwDAO.OportunidadeVWDAO()
    return resultado.dictOportunidadeVW(request.json)


@app.route("/fieldsOportunidadeVW/", methods=["POST"])
def fieldsOportunidadeVW():
    resultado = oportunidadevwDAO.OportunidadeVWDAO()
    return resultado.fieldsOportunidadeVW(request.json)


@app.route("/findOportunidadeVW/", methods=["POST"])
def findOportunidadeVW():
    resultado = oportunidadevwDAO.OportunidadeVWDAO()
    return resultado.findOportunidadeVW(request.json)


"""
  Fim rota: OportunidadeVW
"""

"""
  Rotas do WebService para a classe: OportunidadeItem (TB02256)
"""
import oportunidadeitemDAO


@app.route("/listOportunidadeItem/", methods=["POST"])
def listOportunidadeItem():
    resultado = oportunidadeitemDAO.OportunidadeItemDAO()
    return resultado.listOportunidadeItem(request.json)


@app.route("/dictOportunidadeItem/", methods=["POST"])
def dictOportunidadeItem():
    resultado = oportunidadeitemDAO.OportunidadeItemDAO()
    return resultado.dictOportunidadeItem(request.json)


@app.route("/fieldsOportunidadeItem/", methods=["POST"])
def fieldsOportunidadeItem():
    resultado = oportunidadeitemDAO.OportunidadeItemDAO()
    return resultado.fieldsOportunidadeItem(request.json)


@app.route("/findOportunidadeItem/", methods=["POST"])
def findOportunidadeItem():
    resultado = oportunidadeitemDAO.OportunidadeItemDAO()
    return resultado.findOportunidadeItem(request.json)


@app.route("/insOportunidadeItem", methods=["POST"])
def insOportunidadeItem():
    resultado = oportunidadeitemDAO.OportunidadeItemDAO()
    return resultado.insOportunidadeItem(request.json)


@app.route("/updOportunidadeItem", methods=["POST"])
def updOportunidadeItem():
    resultado = oportunidadeitemDAO.OportunidadeItemDAO()
    return resultado.updOportunidadeItem(request.json)


@app.route("/delOportunidadeItem", methods=["POST"])
def delOportunidadeItem():
    resultado = oportunidadeitemDAO.OportunidadeItemDAO()
    return resultado.delOportunidadeItem(request.json)


"""
  Fim rota: OportunidadeItem
"""

"""
  Rotas do WebService para a classe: OportunidadeItemVW (VW02274)
"""
import oportunidadeitemvwDAO


@app.route("/listOportunidadeItemVW/", methods=["POST"])
def listOportunidadeItemVW():
    resultado = oportunidadeitemvwDAO.OportunidadeItemVWDAO()
    return resultado.listOportunidadeItemVW(request.json)


@app.route("/dictOportunidadeItemVW/", methods=["POST"])
def dictOportunidadeItemVW():
    resultado = oportunidadeitemvwDAO.OportunidadeItemVWDAO()
    return resultado.dictOportunidadeItemVW(request.json)


@app.route("/fieldsOportunidadeItemVW/", methods=["POST"])
def fieldsOportunidadeItemVW():
    resultado = oportunidadeitemvwDAO.OportunidadeItemVWDAO()
    return resultado.fieldsOportunidadeItemVW(request.json)


@app.route("/findOportunidadeItemVW/", methods=["POST"])
def findOportunidadeItemVW():
    resultado = oportunidadeitemvwDAO.OportunidadeItemVWDAO()
    return resultado.findOportunidadeItemVW(request.json)


"""
  Fim rota: OportunidadeItemVW
"""

"""
  Rotas do WebService para a classe: OportunidadeHistorico (TB02257)
"""
import oportunidadehistoricoDAO


@app.route("/listOportunidadeHistorico/", methods=["POST"])
def listOportunidadeHistorico():
    resultado = oportunidadehistoricoDAO.OportunidadeHistoricoDAO()
    return resultado.listOportunidadeHistorico(request.json)


@app.route("/dictOportunidadeHistorico/", methods=["POST"])
def dictOportunidadeHistorico():
    resultado = oportunidadehistoricoDAO.OportunidadeHistoricoDAO()
    return resultado.dictOportunidadeHistorico(request.json)


@app.route("/fieldsOportunidadeHistorico/", methods=["POST"])
def fieldsOportunidadeHistorico():
    resultado = oportunidadehistoricoDAO.OportunidadeHistoricoDAO()
    return resultado.fieldsOportunidadeHistorico(request.json)


@app.route("/findOportunidadeHistorico/", methods=["POST"])
def findOportunidadeHistorico():
    resultado = oportunidadehistoricoDAO.OportunidadeHistoricoDAO()
    return resultado.findOportunidadeHistorico(request.json)


@app.route("/insOportunidadeHistorico", methods=["POST"])
def insOportunidadeHistorico():
    resultado = oportunidadehistoricoDAO.OportunidadeHistoricoDAO()
    return resultado.insOportunidadeHistorico(request.json)


@app.route("/updOportunidadeHistorico", methods=["POST"])
def updOportunidadeHistorico():
    resultado = oportunidadehistoricoDAO.OportunidadeHistoricoDAO()
    return resultado.updOportunidadeHistorico(request.json)


@app.route("/delOportunidadeHistorico", methods=["POST"])
def delOportunidadeHistorico():
    resultado = oportunidadehistoricoDAO.OportunidadeHistoricoDAO()
    return resultado.delOportunidadeHistorico(request.json)


"""
  Fim rota: OportunidadeHistorico
"""

"""
  Rotas do WebService para a classe: OportunidadeHistoricoVW (VW02275)
"""
import oportunidadehistoricovwDAO


@app.route("/listOportunidadeHistoricoVW/", methods=["POST"])
def listOportunidadeHistoricoVW():
    resultado = oportunidadehistoricovwDAO.OportunidadeHistoricoVWDAO()
    return resultado.listOportunidadeHistoricoVW(request.json)


@app.route("/dictOportunidadeHistoricoVW/", methods=["POST"])
def dictOportunidadeHistoricoVW():
    resultado = oportunidadehistoricovwDAO.OportunidadeHistoricoVWDAO()
    return resultado.dictOportunidadeHistoricoVW(request.json)


@app.route("/fieldsOportunidadeHistoricoVW/", methods=["POST"])
def fieldsOportunidadeHistoricoVW():
    resultado = oportunidadehistoricovwDAO.OportunidadeHistoricoVWDAO()
    return resultado.fieldsOportunidadeHistoricoVW(request.json)


@app.route("/findOportunidadeHistoricoVW/", methods=["POST"])
def findOportunidadeHistoricoVW():
    resultado = oportunidadehistoricovwDAO.OportunidadeHistoricoVWDAO()
    return resultado.findOportunidadeHistoricoVW(request.json)


"""
  Fim rota: OportunidadeHistoricoVW
"""

"""
  Rotas do WebService para a classe: PropostaItem (TB02258)
"""
import propostaitemDAO


@app.route("/listPropostaItem/", methods=["POST"])
def listPropostaItem():
    resultado = propostaitemDAO.PropostaItemDAO()
    return resultado.listPropostaItem(request.json)


@app.route("/dictPropostaItem/", methods=["POST"])
def dictPropostaItem():
    resultado = propostaitemDAO.PropostaItemDAO()
    return resultado.dictPropostaItem(request.json)


@app.route("/fieldsPropostaItem/", methods=["POST"])
def fieldsPropostaItem():
    resultado = propostaitemDAO.PropostaItemDAO()
    return resultado.fieldsPropostaItem(request.json)


@app.route("/findPropostaItem/", methods=["POST"])
def findPropostaItem():
    resultado = propostaitemDAO.PropostaItemDAO()
    return resultado.findPropostaItem(request.json)


@app.route("/insPropostaItem", methods=["POST"])
def insPropostaItem():
    resultado = propostaitemDAO.PropostaItemDAO()
    return resultado.insPropostaItem(request.json)


@app.route("/updPropostaItem", methods=["POST"])
def updPropostaItem():
    resultado = propostaitemDAO.PropostaItemDAO()
    return resultado.updPropostaItem(request.json)


@app.route("/delPropostaItem", methods=["POST"])
def delPropostaItem():
    resultado = propostaitemDAO.PropostaItemDAO()
    return resultado.delPropostaItem(request.json)


"""
  Fim rota: PropostaItem
"""

"""
  Rotas do WebService para a classe: PropostaItemVW (VW02276)
"""
import propostaitemvwDAO


@app.route("/listPropostaItemVW/", methods=["POST"])
def listPropostaItemVW():
    resultado = propostaitemvwDAO.PropostaItemVWDAO()
    return resultado.listPropostaItemVW(request.json)


@app.route("/dictPropostaItemVW/", methods=["POST"])
def dictPropostaItemVW():
    resultado = propostaitemvwDAO.PropostaItemVWDAO()
    return resultado.dictPropostaItemVW(request.json)


@app.route("/fieldsPropostaItemVW/", methods=["POST"])
def fieldsPropostaItemVW():
    resultado = propostaitemvwDAO.PropostaItemVWDAO()
    return resultado.fieldsPropostaItemVW(request.json)


@app.route("/findPropostaItemVW/", methods=["POST"])
def findPropostaItemVW():
    resultado = propostaitemvwDAO.PropostaItemVWDAO()
    return resultado.findPropostaItemVW(request.json)


"""
  Fim rota: PropostaItemVW
"""

"""
  Rotas do WebService para a classe: PropostaComissao (TB02259)
"""
import propostacomissaoDAO


@app.route("/listPropostaComissao/", methods=["POST"])
def listPropostaComissao():
    resultado = propostacomissaoDAO.PropostaComissaoDAO()
    return resultado.listPropostaComissao(request.json)


@app.route("/dictPropostaComissao/", methods=["POST"])
def dictPropostaComissao():
    resultado = propostacomissaoDAO.PropostaComissaoDAO()
    return resultado.dictPropostaComissao(request.json)


@app.route("/fieldsPropostaComissao/", methods=["POST"])
def fieldsPropostaComissao():
    resultado = propostacomissaoDAO.PropostaComissaoDAO()
    return resultado.fieldsPropostaComissao(request.json)


@app.route("/findPropostaComissao/", methods=["POST"])
def findPropostaComissao():
    resultado = propostacomissaoDAO.PropostaComissaoDAO()
    return resultado.findPropostaComissao(request.json)


@app.route("/insPropostaComissao", methods=["POST"])
def insPropostaComissao():
    resultado = propostacomissaoDAO.PropostaComissaoDAO()
    return resultado.insPropostaComissao(request.json)


@app.route("/updPropostaComissao", methods=["POST"])
def updPropostaComissao():
    resultado = propostacomissaoDAO.PropostaComissaoDAO()
    return resultado.updPropostaComissao(request.json)


@app.route("/delPropostaComissao", methods=["POST"])
def delPropostaComissao():
    resultado = propostacomissaoDAO.PropostaComissaoDAO()
    return resultado.delPropostaComissao(request.json)


"""
  Fim rota: PropostaComissao
"""

"""
  Rotas do WebService para a classe: PropostaComissaoVW (VW02277)
"""
import propostacomissaovwDAO


@app.route("/listPropostaComissaoVW/", methods=["POST"])
def listPropostaComissaoVW():
    resultado = propostacomissaovwDAO.PropostaComissaoVWDAO()
    return resultado.listPropostaComissaoVW(request.json)


@app.route("/dictPropostaComissaoVW/", methods=["POST"])
def dictPropostaComissaoVW():
    resultado = propostacomissaovwDAO.PropostaComissaoVWDAO()
    return resultado.dictPropostaComissaoVW(request.json)


@app.route("/fieldsPropostaComissaoVW/", methods=["POST"])
def fieldsPropostaComissaoVW():
    resultado = propostacomissaovwDAO.PropostaComissaoVWDAO()
    return resultado.fieldsPropostaComissaoVW(request.json)


"""
  Fim rota: PropostaComissaoVW
"""

"""
  Rotas do WebService para a classe: PropostaContrato (TB02260)
"""
import propostacontratoDAO


@app.route("/listPropostaContrato/", methods=["POST"])
def listPropostaContrato():
    resultado = propostacontratoDAO.PropostaContratoDAO()
    return resultado.listPropostaContrato(request.json)


@app.route("/dictPropostaContrato/", methods=["POST"])
def dictPropostaContrato():
    resultado = propostacontratoDAO.PropostaContratoDAO()
    return resultado.dictPropostaContrato(request.json)


@app.route("/fieldsPropostaContrato/", methods=["POST"])
def fieldsPropostaContrato():
    resultado = propostacontratoDAO.PropostaContratoDAO()
    return resultado.fieldsPropostaContrato(request.json)


@app.route("/findPropostaContrato/", methods=["POST"])
def findPropostaContrato():
    resultado = propostacontratoDAO.PropostaContratoDAO()
    return resultado.findPropostaContrato(request.json)


@app.route("/propostacontratoID", methods=["POST"])
def propostacontratoID():
    resultado = propostacontratoDAO.PropostaContratoDAO()
    return resultado.propostacontratoID(request.json)


@app.route("/insPropostaContrato", methods=["POST"])
def insPropostaContrato():
    resultado = propostacontratoDAO.PropostaContratoDAO()
    return resultado.insPropostaContrato(request.json)


@app.route("/updPropostaContrato", methods=["POST"])
def updPropostaContrato():
    resultado = propostacontratoDAO.PropostaContratoDAO()
    return resultado.updPropostaContrato(request.json)


@app.route("/delPropostaContrato", methods=["POST"])
def delPropostaContrato():
    resultado = propostacontratoDAO.PropostaContratoDAO()
    return resultado.delPropostaContrato(request.json)


"""
  Fim rota: PropostaContrato
"""

"""
  Rotas do WebService para a classe: PropostaEquipamento (TB02261)
"""
import propostaequipamentoDAO


@app.route("/listPropostaEquipamento/", methods=["POST"])
def listPropostaEquipamento():
    resultado = propostaequipamentoDAO.PropostaEquipamentoDAO()
    return resultado.listPropostaEquipamento(request.json)


@app.route("/dictPropostaEquipamento/", methods=["POST"])
def dictPropostaEquipamento():
    resultado = propostaequipamentoDAO.PropostaEquipamentoDAO()
    return resultado.dictPropostaEquipamento(request.json)


@app.route("/fieldsPropostaEquipamento/", methods=["POST"])
def fieldsPropostaEquipamento():
    resultado = propostaequipamentoDAO.PropostaEquipamentoDAO()
    return resultado.fieldsPropostaEquipamento(request.json)


@app.route("/findPropostaEquipamento/", methods=["POST"])
def findPropostaEquipamento():
    resultado = propostaequipamentoDAO.PropostaEquipamentoDAO()
    return resultado.findPropostaEquipamento(request.json)


@app.route("/PropostaEquipamentoID", methods=["POST"])
def propostaequipamentoID():
    resultado = propostaequipamentoDAO.PropostaEquipamentoDAO()
    return resultado.propostaequipamentoID(request.json)


@app.route("/insPropostaEquipamento", methods=["POST"])
def insPropostaEquipamento():
    resultado = propostaequipamentoDAO.PropostaEquipamentoDAO()
    return resultado.insPropostaEquipamento(request.json)


@app.route("/updPropostaEquipamento", methods=["POST"])
def updPropostaEquipamento():
    resultado = propostaequipamentoDAO.PropostaEquipamentoDAO()
    return resultado.updPropostaEquipamento(request.json)


@app.route("/delPropostaEquipamento", methods=["POST"])
def delPropostaEquipamento():
    resultado = propostaequipamentoDAO.PropostaEquipamentoDAO()
    return resultado.delPropostaEquipamento(request.json)


"""
  Fim rota: PropostaEquipamento
"""

"""
  Rotas do WebService para a classe: PropostaEquipamentoVW (VW02279)
"""
import propostaequipamentovwDAO


@app.route("/listPropostaEquipamentoVW/", methods=["POST"])
def listPropostaEquipamentoVW():
    resultado = propostaequipamentovwDAO.PropostaEquipamentoVWDAO()
    return resultado.listPropostaEquipamentoVW(request.json)


@app.route("/dictPropostaEquipamentoVW/", methods=["POST"])
def dictPropostaEquipamentoVW():
    resultado = propostaequipamentovwDAO.PropostaEquipamentoVWDAO()
    return resultado.dictPropostaEquipamentoVW(request.json)


@app.route("/fieldsPropostaEquipamentoVW/", methods=["POST"])
def fieldsPropostaEquipamentoVW():
    resultado = propostaequipamentovwDAO.PropostaEquipamentoVWDAO()
    return resultado.fieldsPropostaEquipamentoVW(request.json)


@app.route("/findPropostaEquipamentoVW/", methods=["POST"])
def findPropostaEquipamentoVW():
    resultado = propostaequipamentovwDAO.PropostaEquipamentoVWDAO()
    return resultado.findPropostaEquipamentoVW(request.json)


@app.route("/propostaequipamentovwID", methods=["POST"])
def propostaequipamentovwID():
    resultado = propostaequipamentovwDAO.PropostaEquipamentoVWDAO()
    return resultado.propostaequipamentovwID(request.json)


"""
  Fim rota: PropostaEquipamentoVW
"""

"""
  Rotas do WebService para a classe: PropostaEquipamentoTotal (TB02262)
"""
import propostaequipamentototalDAO


@app.route("/listPropostaEquipamentoTotal/", methods=["POST"])
def listPropostaEquipamentoTotal():
    resultado = propostaequipamentototalDAO.PropostaEquipamentoTotalDAO()
    return resultado.listPropostaEquipamentoTotal(request.json)


@app.route("/dictPropostaEquipamentoTotal/", methods=["POST"])
def dictPropostaEquipamentoTotal():
    resultado = propostaequipamentototalDAO.PropostaEquipamentoTotalDAO()
    return resultado.dictPropostaEquipamentoTotal(request.json)


@app.route("/fieldsPropostaEquipamentoTotal/", methods=["POST"])
def fieldsPropostaEquipamentoTotal():
    resultado = propostaequipamentototalDAO.PropostaEquipamentoTotalDAO()
    return resultado.fieldsPropostaEquipamentoTotal(request.json)


@app.route("/findPropostaEquipamentoTotal/", methods=["POST"])
def findPropostaEquipamentoTotal():
    resultado = propostaequipamentototalDAO.PropostaEquipamentoTotalDAO()
    return resultado.findPropostaEquipamentoTotal(request.json)


"""
  Fim rota: PropostaEquipamentoTotal
"""

"""
  Rotas do WebService para a classe: PropostaEndereco (TB02263)
"""
import propostaenderecoDAO


@app.route("/listPropostaEndereco/", methods=["POST"])
def listPropostaEndereco():
    resultado = propostaenderecoDAO.PropostaEnderecoDAO()
    return resultado.listPropostaEndereco(request.json)


@app.route("/dictPropostaEndereco/", methods=["POST"])
def dictPropostaEndereco():
    resultado = propostaenderecoDAO.PropostaEnderecoDAO()
    return resultado.dictPropostaEndereco(request.json)


@app.route("/fieldsPropostaEndereco/", methods=["POST"])
def fieldsPropostaEndereco():
    resultado = propostaenderecoDAO.PropostaEnderecoDAO()
    return resultado.fieldsPropostaEndereco(request.json)


@app.route("/findPropostaEndereco/", methods=["POST"])
def findPropostaEndereco():
    resultado = propostaenderecoDAO.PropostaEnderecoDAO()
    return resultado.findPropostaEndereco(request.json)


@app.route("/PropostaEnderecoID", methods=["POST"])
def propostaenderecoID():
    resultado = propostaenderecoDAO.PropostaEnderecoDAO()
    return resultado.propostaenderecoID(request.json)


@app.route("/insPropostaEndereco", methods=["POST"])
def insPropostaEndereco():
    resultado = propostaenderecoDAO.PropostaEnderecoDAO()
    return resultado.insPropostaEndereco(request.json)


@app.route("/updPropostaEndereco", methods=["POST"])
def updPropostaEndereco():
    resultado = propostaenderecoDAO.PropostaEnderecoDAO()
    return resultado.updPropostaEndereco(request.json)


@app.route("/delPropostaEndereco", methods=["POST"])
def delPropostaEndereco():
    resultado = propostaenderecoDAO.PropostaEnderecoDAO()
    return resultado.delPropostaEndereco(request.json)


"""
  Fim rota: PropostaEndereco
"""

"""
  Rotas do WebService para a classe: PrecontratoStatus (TB01136)
"""
import precontratostatusDAO


@app.route("/listPrecontratoStatus/", methods=["POST"])
def listPrecontratoStatus():
    resultado = precontratostatusDAO.PrecontratoStatusDAO()
    return resultado.listPrecontratoStatus(request.json)


@app.route("/dictPrecontratoStatus/", methods=["POST"])
def dictPrecontratoStatus():
    resultado = precontratostatusDAO.PrecontratoStatusDAO()
    return resultado.dictPrecontratoStatus(request.json)


@app.route("/fieldsPrecontratoStatus/", methods=["POST"])
def fieldsPrecontratoStatus():
    resultado = precontratostatusDAO.PrecontratoStatusDAO()
    return resultado.fieldsPrecontratoStatus(request.json)


@app.route("/findPrecontratoStatus/", methods=["POST"])
def findPrecontratoStatus():
    resultado = precontratostatusDAO.PrecontratoStatusDAO()
    return resultado.findPrecontratoStatus(request.json)


@app.route("/PrecontratoStatusID", methods=["POST"])
def precontratostatusID():
    resultado = precontratostatusDAO.PrecontratoStatusDAO()
    return resultado.precontratostatusID(request.json)


@app.route("/insPrecontratoStatus", methods=["POST"])
def insPrecontratoStatus():
    resultado = precontratostatusDAO.PrecontratoStatusDAO()
    return resultado.insPrecontratoStatus(request.json)


@app.route("/updPrecontratoStatus", methods=["POST"])
def updPrecontratoStatus():
    resultado = precontratostatusDAO.PrecontratoStatusDAO()
    return resultado.updPrecontratoStatus(request.json)


@app.route("/delPrecontratoStatus", methods=["POST"])
def delPrecontratoStatus():
    resultado = precontratostatusDAO.PrecontratoStatusDAO()
    return resultado.delPrecontratoStatus(request.json)


"""
  Fim rota: PrecontratoStatus
"""

"""
  Rotas do WebService para a classe: PrecontratoWorkflow (TB01137)
"""
import precontratoworkflowDAO


@app.route("/listPrecontratoWorkflow/", methods=["POST"])
def listPrecontratoWorkflow():
    resultado = precontratoworkflowDAO.PrecontratoWorkflowDAO()
    return resultado.listPrecontratoWorkflow(request.json)


@app.route("/dictPrecontratoWorkflow/", methods=["POST"])
def dictPrecontratoWorkflow():
    resultado = precontratoworkflowDAO.PrecontratoWorkflowDAO()
    return resultado.dictPrecontratoWorkflow(request.json)


@app.route("/fieldsPrecontratoWorkflow/", methods=["POST"])
def fieldsPrecontratoWorkflow():
    resultado = precontratoworkflowDAO.PrecontratoWorkflowDAO()
    return resultado.fieldsPrecontratoWorkflow(request.json)


@app.route("/findPrecontratoWorkflow/", methods=["POST"])
def findPrecontratoWorkflow():
    resultado = precontratoworkflowDAO.PrecontratoWorkflowDAO()
    return resultado.findPrecontratoWorkflow(request.json)


@app.route("/insPrecontratoWorkflow", methods=["POST"])
def insPrecontratoWorkflow():
    resultado = precontratoworkflowDAO.PrecontratoWorkflowDAO()
    return resultado.insPrecontratoWorkflow(request.json)


@app.route("/updPrecontratoWorkflow", methods=["POST"])
def updPrecontratoWorkflow():
    resultado = precontratoworkflowDAO.PrecontratoWorkflowDAO()
    return resultado.updPrecontratoWorkflow(request.json)


@app.route("/delPrecontratoWorkflow", methods=["POST"])
def delPrecontratoWorkflow():
    resultado = precontratoworkflowDAO.PrecontratoWorkflowDAO()
    return resultado.delPrecontratoWorkflow(request.json)


"""
  Fim rota: PrecontratoWorkflow
"""

"""
  Rotas do WebService para a classe: PrecontratoWorkflowVW (VW01128)
"""
import precontratoworkflowvwDAO


@app.route("/listPrecontratoWorkflowVW/", methods=["POST"])
def listPrecontratoWorkflowVW():
    resultado = precontratoworkflowvwDAO.PrecontratoWorkflowVWDAO()
    return resultado.listPrecontratoWorkflowVW(request.json)


@app.route("/dictPrecontratoWorkflowVW/", methods=["POST"])
def dictPrecontratoWorkflowVW():
    resultado = precontratoworkflowvwDAO.PrecontratoWorkflowVWDAO()
    return resultado.dictPrecontratoWorkflowVW(request.json)


@app.route("/fieldsPrecontratoWorkflowVW/", methods=["POST"])
def fieldsPrecontratoWorkflowVW():
    resultado = precontratoworkflowvwDAO.PrecontratoWorkflowVWDAO()
    return resultado.fieldsPrecontratoWorkflowVW(request.json)


@app.route("/findPrecontratoWorkflowVW/", methods=["POST"])
def findPrecontratoWorkflowVW():
    resultado = precontratoworkflowvwDAO.PrecontratoWorkflowVWDAO()
    return resultado.findPrecontratoWorkflowVW(request.json)


"""
  Fim rota: PrecontratoWorkflowVW
"""

"""
  Rotas do WebService para a classe: Precontrato (TB02264)
"""
import precontratoDAO


@app.route("/listPrecontrato/", methods=["POST"])
def listPrecontrato():
    resultado = precontratoDAO.PrecontratoDAO()
    return resultado.listPrecontrato(request.json)


@app.route("/dictPrecontrato/", methods=["POST"])
def dictPrecontrato():
    resultado = precontratoDAO.PrecontratoDAO()
    return resultado.dictPrecontrato(request.json)


@app.route("/fieldsPrecontrato/", methods=["POST"])
def fieldsPrecontrato():
    resultado = precontratoDAO.PrecontratoDAO()
    return resultado.fieldsPrecontrato(request.json)


@app.route("/findPrecontrato/", methods=["POST"])
def findPrecontrato():
    resultado = precontratoDAO.PrecontratoDAO()
    return resultado.findPrecontrato(request.json)


@app.route("/PrecontratoID", methods=["POST"])
def precontratoID():
    resultado = precontratoDAO.PrecontratoDAO()
    return resultado.precontratoID(request.json)


@app.route("/insPrecontrato", methods=["POST"])
def insPrecontrato():
    resultado = precontratoDAO.PrecontratoDAO()
    return resultado.insPrecontrato(request.json)


@app.route("/updPrecontrato", methods=["POST"])
def updPrecontrato():
    resultado = precontratoDAO.PrecontratoDAO()
    return resultado.updPrecontrato(request.json)


@app.route("/delPrecontrato", methods=["POST"])
def delPrecontrato():
    resultado = precontratoDAO.PrecontratoDAO()
    return resultado.delPrecontrato(request.json)


"""
  Fim rota: Precontrato
"""

"""
  Rotas do WebService para a classe: PrecontratoVW (VW02280)
"""
import precontratovwDAO


@app.route("/listPrecontratoVW/", methods=["POST"])
def listPrecontratoVW():
    resultado = precontratovwDAO.PrecontratoVWDAO()
    return resultado.listPrecontratoVW(request.json)


@app.route("/dictPrecontratoVW/", methods=["POST"])
def dictPrecontratoVW():
    resultado = precontratovwDAO.PrecontratoVWDAO()
    return resultado.dictPrecontratoVW(request.json)


@app.route("/fieldsPrecontratoVW/", methods=["POST"])
def fieldsPrecontratoVW():
    resultado = precontratovwDAO.PrecontratoVWDAO()
    return resultado.fieldsPrecontratoVW(request.json)


@app.route("/findPrecontratoVW/", methods=["POST"])
def findPrecontratoVW():
    resultado = precontratovwDAO.PrecontratoVWDAO()
    return resultado.findPrecontratoVW(request.json)


"""
  Fim rota: PrecontratoVW
"""

"""
  Rotas do WebService para a classe: PrecontratoItem (TB02265)
"""
import precontratoitemDAO


@app.route("/listPrecontratoItem/", methods=["POST"])
def listPrecontratoItem():
    resultado = precontratoitemDAO.PrecontratoItemDAO()
    return resultado.listPrecontratoItem(request.json)


@app.route("/dictPrecontratoItem/", methods=["POST"])
def dictPrecontratoItem():
    resultado = precontratoitemDAO.PrecontratoItemDAO()
    return resultado.dictPrecontratoItem(request.json)


@app.route("/fieldsPrecontratoItem/", methods=["POST"])
def fieldsPrecontratoItem():
    resultado = precontratoitemDAO.PrecontratoItemDAO()
    return resultado.fieldsPrecontratoItem(request.json)


@app.route("/findPrecontratoItem/", methods=["POST"])
def findPrecontratoItem():
    resultado = precontratoitemDAO.PrecontratoItemDAO()
    return resultado.findPrecontratoItem(request.json)


@app.route("/insPrecontratoItem", methods=["POST"])
def insPrecontratoItem():
    resultado = precontratoitemDAO.PrecontratoItemDAO()
    return resultado.insPrecontratoItem(request.json)


@app.route("/updPrecontratoItem", methods=["POST"])
def updPrecontratoItem():
    resultado = precontratoitemDAO.PrecontratoItemDAO()
    return resultado.updPrecontratoItem(request.json)


@app.route("/delPrecontratoItem", methods=["POST"])
def delPrecontratoItem():
    resultado = precontratoitemDAO.PrecontratoItemDAO()
    return resultado.delPrecontratoItem(request.json)


"""
  Fim rota: PrecontratoItem
"""

"""
  Rotas do WebService para a classe: PrecontratoItemVW (VW02281)
"""
import precontratoitemvwDAO


@app.route("/listPrecontratoItemVW/", methods=["POST"])
def listPrecontratoItemVW():
    resultado = precontratoitemvwDAO.PrecontratoItemVWDAO()
    return resultado.listPrecontratoItemVW(request.json)


@app.route("/dictPrecontratoItemVW/", methods=["POST"])
def dictPrecontratoItemVW():
    resultado = precontratoitemvwDAO.PrecontratoItemVWDAO()
    return resultado.dictPrecontratoItemVW(request.json)


@app.route("/fieldsPrecontratoItemVW/", methods=["POST"])
def fieldsPrecontratoItemVW():
    resultado = precontratoitemvwDAO.PrecontratoItemVWDAO()
    return resultado.fieldsPrecontratoItemVW(request.json)


@app.route("/findPrecontratoItemVW/", methods=["POST"])
def findPrecontratoItemVW():
    resultado = precontratoitemvwDAO.PrecontratoItemVWDAO()
    return resultado.findPrecontratoItemVW(request.json)


"""
  Fim rota: PrecontratoItemVW
"""

"""
  Rotas do WebService para a classe: PrecontratoHistorico (TB02266)
"""
import precontratohistoricoDAO


@app.route("/listPrecontratoHistorico/", methods=["POST"])
def listPrecontratoHistorico():
    resultado = precontratohistoricoDAO.PrecontratoHistoricoDAO()
    return resultado.listPrecontratoHistorico(request.json)


@app.route("/dictPrecontratoHistorico/", methods=["POST"])
def dictPrecontratoHistorico():
    resultado = precontratohistoricoDAO.PrecontratoHistoricoDAO()
    return resultado.dictPrecontratoHistorico(request.json)


@app.route("/fieldsPrecontratoHistorico/", methods=["POST"])
def fieldsPrecontratoHistorico():
    resultado = precontratohistoricoDAO.PrecontratoHistoricoDAO()
    return resultado.fieldsPrecontratoHistorico(request.json)


@app.route("/findPrecontratoHistorico/", methods=["POST"])
def findPrecontratoHistorico():
    resultado = precontratohistoricoDAO.PrecontratoHistoricoDAO()
    return resultado.findPrecontratoHistorico(request.json)


@app.route("/insPrecontratoHistorico", methods=["POST"])
def insPrecontratoHistorico():
    resultado = precontratohistoricoDAO.PrecontratoHistoricoDAO()
    return resultado.insPrecontratoHistorico(request.json)


@app.route("/updPrecontratoHistorico", methods=["POST"])
def updPrecontratoHistorico():
    resultado = precontratohistoricoDAO.PrecontratoHistoricoDAO()
    return resultado.updPrecontratoHistorico(request.json)


@app.route("/delPrecontratoHistorico", methods=["POST"])
def delPrecontratoHistorico():
    resultado = precontratohistoricoDAO.PrecontratoHistoricoDAO()
    return resultado.delPrecontratoHistorico(request.json)


"""
  Fim rota: PrecontratoHistorico
"""

"""
  Rotas do WebService para a classe: PrecontratoHistoricoVW (VW02282)
"""
import precontratohistoricovwDAO


@app.route("/listPrecontratoHistoricoVW/", methods=["POST"])
def listPrecontratoHistoricoVW():
    resultado = precontratohistoricovwDAO.PrecontratoHistoricoVWDAO()
    return resultado.listPrecontratoHistoricoVW(request.json)


@app.route("/dictPrecontratoHistoricoVW/", methods=["POST"])
def dictPrecontratoHistoricoVW():
    resultado = precontratohistoricovwDAO.PrecontratoHistoricoVWDAO()
    return resultado.dictPrecontratoHistoricoVW(request.json)


@app.route("/fieldsPrecontratoHistoricoVW/", methods=["POST"])
def fieldsPrecontratoHistoricoVW():
    resultado = precontratohistoricovwDAO.PrecontratoHistoricoVWDAO()
    return resultado.fieldsPrecontratoHistoricoVW(request.json)


@app.route("/findPrecontratoHistoricoVW/", methods=["POST"])
def findPrecontratoHistoricoVW():
    resultado = precontratohistoricovwDAO.PrecontratoHistoricoVWDAO()
    return resultado.findPrecontratoHistoricoVW(request.json)


"""
  Fim rota: PrecontratoHistoricoVW
"""

"""
  Rotas do WebService para a classe: PrecontratoEquipamentoVW (VW02283)
"""
import precontratoequipamentovwDAO


@app.route("/listPrecontratoEquipamentoVW/", methods=["POST"])
def listPrecontratoEquipamentoVW():
    resultado = precontratoequipamentovwDAO.PrecontratoEquipamentoVWDAO()
    return resultado.listPrecontratoEquipamentoVW(request.json)


@app.route("/dictPrecontratoEquipamentoVW/", methods=["POST"])
def dictPrecontratoEquipamentoVW():
    resultado = precontratoequipamentovwDAO.PrecontratoEquipamentoVWDAO()
    return resultado.dictPrecontratoEquipamentoVW(request.json)


@app.route("/fieldsPrecontratoEquipamentoVW/", methods=["POST"])
def fieldsPrecontratoEquipamentoVW():
    resultado = precontratoequipamentovwDAO.PrecontratoEquipamentoVWDAO()
    return resultado.fieldsPrecontratoEquipamentoVW(request.json)


@app.route("/findPrecontratoEquipamentoVW/", methods=["POST"])
def findPrecontratoEquipamentoVW():
    resultado = precontratoequipamentovwDAO.PrecontratoEquipamentoVWDAO()
    return resultado.findPrecontratoEquipamentoVW(request.json)


"""
  Fim rota: PrecontratoEquipamentoVW
"""

"""
  Rotas do WebService para a classe: PrecontratoEquipamentoTotal (TB02268)
"""
import precontratoequipamentototalDAO


@app.route("/listPrecontratoEquipamentoTotal/", methods=["POST"])
def listPrecontratoEquipamentoTotal():
    resultado = precontratoequipamentototalDAO.PrecontratoEquipamentoTotalDAO()
    return resultado.listPrecontratoEquipamentoTotal(request.json)


@app.route("/dictPrecontratoEquipamentoTotal/", methods=["POST"])
def dictPrecontratoEquipamentoTotal():
    resultado = precontratoequipamentototalDAO.PrecontratoEquipamentoTotalDAO()
    return resultado.dictPrecontratoEquipamentoTotal(request.json)


@app.route("/fieldsPrecontratoEquipamentoTotal/", methods=["POST"])
def fieldsPrecontratoEquipamentoTotal():
    resultado = precontratoequipamentototalDAO.PrecontratoEquipamentoTotalDAO()
    return resultado.fieldsPrecontratoEquipamentoTotal(request.json)


@app.route("/findPrecontratoEquipamentoTotal/", methods=["POST"])
def findPrecontratoEquipamentoTotal():
    resultado = precontratoequipamentototalDAO.PrecontratoEquipamentoTotalDAO()
    return resultado.findPrecontratoEquipamentoTotal(request.json)


"""
  Fim rota: PrecontratoEquipamentoTotal
"""

"""
  Rotas do WebService para a classe: PrecontratoEndereco (TB02269)
"""
import precontratoenderecoDAO


@app.route("/listPrecontratoEndereco/", methods=["POST"])
def listPrecontratoEndereco():
    resultado = precontratoenderecoDAO.PrecontratoEnderecoDAO()
    return resultado.listPrecontratoEndereco(request.json)


@app.route("/dictPrecontratoEndereco/", methods=["POST"])
def dictPrecontratoEndereco():
    resultado = precontratoenderecoDAO.PrecontratoEnderecoDAO()
    return resultado.dictPrecontratoEndereco(request.json)


@app.route("/fieldsPrecontratoEndereco/", methods=["POST"])
def fieldsPrecontratoEndereco():
    resultado = precontratoenderecoDAO.PrecontratoEnderecoDAO()
    return resultado.fieldsPrecontratoEndereco(request.json)


@app.route("/findPrecontratoEndereco/", methods=["POST"])
def findPrecontratoEndereco():
    resultado = precontratoenderecoDAO.PrecontratoEnderecoDAO()
    return resultado.findPrecontratoEndereco(request.json)


@app.route("/PrecontratoEnderecoID", methods=["POST"])
def precontratoenderecoID():
    resultado = precontratoenderecoDAO.PrecontratoEnderecoDAO()
    return resultado.precontratoenderecoID(request.json)


@app.route("/insPrecontratoEndereco", methods=["POST"])
def insPrecontratoEndereco():
    resultado = precontratoenderecoDAO.PrecontratoEnderecoDAO()
    return resultado.insPrecontratoEndereco(request.json)


@app.route("/updPrecontratoEndereco", methods=["POST"])
def updPrecontratoEndereco():
    resultado = precontratoenderecoDAO.PrecontratoEnderecoDAO()
    return resultado.updPrecontratoEndereco(request.json)


@app.route("/delPrecontratoEndereco", methods=["POST"])
def delPrecontratoEndereco():
    resultado = precontratoenderecoDAO.PrecontratoEnderecoDAO()
    return resultado.delPrecontratoEndereco(request.json)


"""
  Fim rota: PrecontratoEndereco
"""

"""
  Rotas do WebService para a classe: PrecontratoComissao (TB02273)
"""
import precontratocomissaoDAO


@app.route("/listPrecontratoComissao/", methods=["POST"])
def listPrecontratoComissao():
    resultado = precontratocomissaoDAO.PrecontratoComissaoDAO()
    return resultado.listPrecontratoComissao(request.json)


@app.route("/dictPrecontratoComissao/", methods=["POST"])
def dictPrecontratoComissao():
    resultado = precontratocomissaoDAO.PrecontratoComissaoDAO()
    return resultado.dictPrecontratoComissao(request.json)


@app.route("/fieldsPrecontratoComissao/", methods=["POST"])
def fieldsPrecontratoComissao():
    resultado = precontratocomissaoDAO.PrecontratoComissaoDAO()
    return resultado.fieldsPrecontratoComissao(request.json)


@app.route("/findPrecontratoComissao/", methods=["POST"])
def findPrecontratoComissao():
    resultado = precontratocomissaoDAO.PrecontratoComissaoDAO()
    return resultado.findPrecontratoComissao(request.json)


@app.route("/insPrecontratoComissao", methods=["POST"])
def insPrecontratoComissao():
    resultado = precontratocomissaoDAO.PrecontratoComissaoDAO()
    return resultado.insPrecontratoComissao(request.json)


@app.route("/updPrecontratoComissao", methods=["POST"])
def updPrecontratoComissao():
    resultado = precontratocomissaoDAO.PrecontratoComissaoDAO()
    return resultado.updPrecontratoComissao(request.json)


@app.route("/delPrecontratoComissao", methods=["POST"])
def delPrecontratoComissao():
    resultado = precontratocomissaoDAO.PrecontratoComissaoDAO()
    return resultado.delPrecontratoComissao(request.json)


"""
  Fim rota: PrecontratoComissao
"""

"""
  Rotas do WebService para a classe: PrecontratoComissaoVW (VW02284)
"""
import precontratocomissaovwDAO


@app.route("/listPrecontratoComissaoVW/", methods=["POST"])
def listPrecontratoComissaoVW():
    resultado = precontratocomissaovwDAO.PrecontratoComissaoVWDAO()
    return resultado.listPrecontratoComissaoVW(request.json)


@app.route("/dictPrecontratoComissaoVW/", methods=["POST"])
def dictPrecontratoComissaoVW():
    resultado = precontratocomissaovwDAO.PrecontratoComissaoVWDAO()
    return resultado.dictPrecontratoComissaoVW(request.json)


@app.route("/fieldsPrecontratoComissaoVW/", methods=["POST"])
def fieldsPrecontratoComissaoVW():
    resultado = precontratocomissaovwDAO.PrecontratoComissaoVWDAO()
    return resultado.fieldsPrecontratoComissaoVW(request.json)


@app.route("/findPrecontratoComissaoVW/", methods=["POST"])
def findPrecontratoComissaoVW():
    resultado = precontratocomissaovwDAO.PrecontratoComissaoVWDAO()
    return resultado.findPrecontratoComissaoVW(request.json)


"""
  Fim rota: PrecontratoComissaoVW
"""

"""
  Rotas do WebService para a classe: PrecontratoTipo (TB01138)
"""
import precontratotipoDAO


@app.route("/listPrecontratoTipo/", methods=["POST"])
def listPrecontratoTipo():
    resultado = precontratotipoDAO.PrecontratoTipoDAO()
    return resultado.listPrecontratoTipo(request.json)


@app.route("/dictPrecontratoTipo/", methods=["POST"])
def dictPrecontratoTipo():
    resultado = precontratotipoDAO.PrecontratoTipoDAO()
    return resultado.dictPrecontratoTipo(request.json)


@app.route("/fieldsPrecontratoTipo/", methods=["POST"])
def fieldsPrecontratoTipo():
    resultado = precontratotipoDAO.PrecontratoTipoDAO()
    return resultado.fieldsPrecontratoTipo(request.json)


@app.route("/findPrecontratoTipo/", methods=["POST"])
def findPrecontratoTipo():
    resultado = precontratotipoDAO.PrecontratoTipoDAO()
    return resultado.findPrecontratoTipo(request.json)


@app.route("/PrecontratoTipoID", methods=["POST"])
def precontratotipoID():
    resultado = precontratotipoDAO.PrecontratoTipoDAO()
    return resultado.precontratotipoID(request.json)


@app.route("/insPrecontratoTipo", methods=["POST"])
def insPrecontratoTipo():
    resultado = precontratotipoDAO.PrecontratoTipoDAO()
    return resultado.insPrecontratoTipo(request.json)


@app.route("/updPrecontratoTipo", methods=["POST"])
def updPrecontratoTipo():
    resultado = precontratotipoDAO.PrecontratoTipoDAO()
    return resultado.updPrecontratoTipo(request.json)


@app.route("/delPrecontratoTipo", methods=["POST"])
def delPrecontratoTipo():
    resultado = precontratotipoDAO.PrecontratoTipoDAO()
    return resultado.delPrecontratoTipo(request.json)


"""
  Fim rota: PrecontratoTipo
"""

"""
  Rotas do WebService para a classe: PrecontratoUser (TB01139)
"""
import precontratouserDAO


@app.route("/listPrecontratoUser/", methods=["POST"])
def listPrecontratoUser():
    resultado = precontratouserDAO.PrecontratoUserDAO()
    return resultado.listPrecontratoUser(request.json)


@app.route("/dictPrecontratoUser/", methods=["POST"])
def dictPrecontratoUser():
    resultado = precontratouserDAO.PrecontratoUserDAO()
    return resultado.dictPrecontratoUser(request.json)


@app.route("/fieldsPrecontratoUser/", methods=["POST"])
def fieldsPrecontratoUser():
    resultado = precontratouserDAO.PrecontratoUserDAO()
    return resultado.fieldsPrecontratoUser(request.json)


@app.route("/findPrecontratoUser/", methods=["POST"])
def findPrecontratoUser():
    resultado = precontratouserDAO.PrecontratoUserDAO()
    return resultado.findPrecontratoUser(request.json)


@app.route("/insPrecontratoUser", methods=["POST"])
def insPrecontratoUser():
    resultado = precontratouserDAO.PrecontratoUserDAO()
    return resultado.insPrecontratoUser(request.json)


@app.route("/updPrecontratoUser", methods=["POST"])
def updPrecontratoUser():
    resultado = precontratouserDAO.PrecontratoUserDAO()
    return resultado.updPrecontratoUser(request.json)


@app.route("/delPrecontratoUser", methods=["POST"])
def delPrecontratoUser():
    resultado = precontratouserDAO.PrecontratoUserDAO()
    return resultado.delPrecontratoUser(request.json)


"""
  Fim rota: PrecontratoUser
"""

"""
  Rotas do WebService para a classe: PrecontratoTipoVW (VW01129)
"""
import precontratotipovwDAO


@app.route("/listPrecontratoTipoVW/", methods=["POST"])
def listPrecontratoTipoVW():
    resultado = precontratotipovwDAO.PrecontratoTipoVWDAO()
    return resultado.listPrecontratoTipoVW(request.json)


@app.route("/dictPrecontratoTipoVW/", methods=["POST"])
def dictPrecontratoTipoVW():
    resultado = precontratotipovwDAO.PrecontratoTipoVWDAO()
    return resultado.dictPrecontratoTipoVW(request.json)


@app.route("/fieldsPrecontratoTipoVW/", methods=["POST"])
def fieldsPrecontratoTipoVW():
    resultado = precontratotipovwDAO.PrecontratoTipoVWDAO()
    return resultado.fieldsPrecontratoTipoVW(request.json)


@app.route("/findPrecontratoTipoVW/", methods=["POST"])
def findPrecontratoTipoVW():
    resultado = precontratotipovwDAO.PrecontratoTipoVWDAO()
    return resultado.findPrecontratoTipoVW(request.json)


"""
  Fim rota: PrecontratoTipoVW
"""

"""
  Rotas do WebService para a classe: PrecontratoEquipamento (TB02267)
"""
import precontratoequipamentoDAO


@app.route("/listPrecontratoEquipamento/", methods=["POST"])
def listPrecontratoEquipamento():
    resultado = precontratoequipamentoDAO.PrecontratoEquipamentoDAO()
    return resultado.listPrecontratoEquipamento(request.json)


@app.route("/dictPrecontratoEquipamento/", methods=["POST"])
def dictPrecontratoEquipamento():
    resultado = precontratoequipamentoDAO.PrecontratoEquipamentoDAO()
    return resultado.dictPrecontratoEquipamento(request.json)


@app.route("/fieldsPrecontratoEquipamento/", methods=["POST"])
def fieldsPrecontratoEquipamento():
    resultado = precontratoequipamentoDAO.PrecontratoEquipamentoDAO()
    return resultado.fieldsPrecontratoEquipamento(request.json)


@app.route("/findPrecontratoEquipamento/", methods=["POST"])
def findPrecontratoEquipamento():
    resultado = precontratoequipamentoDAO.PrecontratoEquipamentoDAO()
    return resultado.findPrecontratoEquipamento(request.json)


@app.route("/PrecontratoEquipamentoID", methods=["POST"])
def precontratoequipamentoID():
    resultado = precontratoequipamentoDAO.PrecontratoEquipamentoDAO()
    return resultado.precontratoequipamentoID(request.json)


@app.route("/insPrecontratoEquipamento", methods=["POST"])
def insPrecontratoEquipamento():
    resultado = precontratoequipamentoDAO.PrecontratoEquipamentoDAO()
    return resultado.insPrecontratoEquipamento(request.json)


@app.route("/updPrecontratoEquipamento", methods=["POST"])
def updPrecontratoEquipamento():
    resultado = precontratoequipamentoDAO.PrecontratoEquipamentoDAO()
    return resultado.updPrecontratoEquipamento(request.json)


@app.route("/delPrecontratoEquipamento", methods=["POST"])
def delPrecontratoEquipamento():
    resultado = precontratoequipamentoDAO.PrecontratoEquipamentoDAO()
    return resultado.delPrecontratoEquipamento(request.json)


"""
  Fim rota: PrecontratoEquipamento
"""

"""
  Rotas do WebService para a classe: UsuarioVW (VW00008)
"""
import usuariovwDAO


@app.route("/listUsuarioVW/", methods=["POST"])
def listUsuarioVW():
    resultado = usuariovwDAO.UsuarioVWDAO()
    return resultado.listUsuarioVW(request.json)


@app.route("/dictUsuarioVW/", methods=["POST"])
def dictUsuarioVW():
    resultado = usuariovwDAO.UsuarioVWDAO()
    return resultado.dictUsuarioVW(request.json)


@app.route("/fieldsUsuarioVW/", methods=["POST"])
def fieldsUsuarioVW():
    resultado = usuariovwDAO.UsuarioVWDAO()
    return resultado.fieldsUsuarioVW(request.json)


"""
  Fim rota: UsuarioVW
"""

"""
  Rotas do WebService para a classe: VendedorVW (VW01002)
"""
import vendedorvwDAO


@app.route("/listVendedorVW/", methods=["POST"])
def listVendedorVW():
    resultado = vendedorvwDAO.VendedorVWDAO()
    return resultado.listVendedorVW(request.json)


@app.route("/dictVendedorVW/", methods=["POST"])
def dictVendedorVW():
    resultado = vendedorvwDAO.VendedorVWDAO()
    return resultado.dictVendedorVW(request.json)


@app.route("/fieldsVendedorVW/", methods=["POST"])
def fieldsVendedorVW():
    resultado = vendedorvwDAO.VendedorVWDAO()
    return resultado.fieldsVendedorVW(request.json)


@app.route("/findVendedorVW/", methods=["POST"])
def findVendedorVW():
    resultado = vendedorvwDAO.VendedorVWDAO()
    return resultado.findVendedorVW(request.json)


"""
  Fim rota: VendedorVW
"""

"""
  Rotas do WebService para a classe: Picture
"""
import picture


@app.route("/getPicture/", methods=["POST"])
def getPicture():
    resultado = picture.Picture()
    return resultado.getPicture(request.json)


@app.route("/getPicturelist/", methods=["POST"])
def getPicturelist():
    resultado = picture.Picture()
    return resultado.getPicturelist(request.json)


@app.route("/setPicture/", methods=["POST"])
def setPicture():
    resultado = picture.Picture()
    return resultado.setPicture(request.json)


"""
  Rotas do WebService para a classe: Usuario (TB00035)
"""

"""
  Rotas do WebService para a classe: File
"""
import files


@app.route("/getFile/", methods=["POST"])
def getFile():
    resultado = files.Files()
    return resultado.getFile(request.json)


@app.route("/setFile/", methods=["POST"])
def setFile():
    resultado = files.Files()
    return resultado.setFile(request.json)


"""
  Rotas do WebService para a classe: Usuario (TB00035)
"""
import usuarioDAO


@app.route("/listUsuario/", methods=["POST"])
def listUsuario():
    resultado = usuarioDAO.UsuarioDAO()
    return resultado.listUsuario(request.json)


@app.route("/dictUsuario/", methods=["POST"])
def dictUsuario():
    resultado = usuarioDAO.UsuarioDAO()
    return resultado.dictUsuario(request.json)


@app.route("/fieldsUsuario/", methods=["POST"])
def fieldsUsuario():
    resultado = usuarioDAO.UsuarioDAO()
    return resultado.fieldsUsuario(request.json)


@app.route("/findUsuario/", methods=["POST"])
def findUsuario():
    resultado = usuarioDAO.UsuarioDAO()
    return resultado.findUsuario(request.json)


@app.route("/UsuarioID", methods=["POST"])
def usuarioID():
    resultado = usuarioDAO.UsuarioDAO()
    return resultado.usuarioID(request.json)


@app.route("/insUsuario", methods=["POST"])
def insUsuario():
    resultado = usuarioDAO.UsuarioDAO()
    return resultado.insUsuario(request.json)


@app.route("/updUsuario", methods=["POST"])
def updUsuario():
    resultado = usuarioDAO.UsuarioDAO()
    return resultado.updUsuario(request.json)


@app.route("/delUsuario", methods=["POST"])
def delUsuario():
    resultado = usuarioDAO.UsuarioDAO()
    return resultado.delUsuario(request.json)


"""
  Fim rota: Usuario
"""

"""
  Rotas do WebService para a classe: Técnico (TB01024)
"""
import técnicoDAO


@app.route("/listTecnico/", methods=["POST"])
def listTécnico():
    resultado = técnicoDAO.TécnicoDAO()
    return resultado.listTécnico(request.json)


@app.route("/dictTecnico/", methods=["POST"])
def dictTécnico():
    resultado = técnicoDAO.TécnicoDAO()
    return resultado.dictTécnico(request.json)


@app.route("/fieldsTecnico/", methods=["POST"])
def fieldsTécnico():
    resultado = técnicoDAO.TécnicoDAO()
    return resultado.fieldsTécnico(request.json)


@app.route("/findTecnico/", methods=["POST"])
def findTécnico():
    resultado = técnicoDAO.TécnicoDAO()
    return resultado.findTécnico(request.json)


@app.route("/TecnicoID", methods=["POST"])
def técnicoID():
    resultado = técnicoDAO.TécnicoDAO()
    return resultado.técnicoID(request.json)


@app.route("/insTecnico", methods=["POST"])
def insTécnico():
    resultado = técnicoDAO.TécnicoDAO()
    return resultado.insTécnico(request.json)


@app.route("/updTecnico", methods=["POST"])
def updTécnico():
    resultado = técnicoDAO.TécnicoDAO()
    return resultado.updTécnico(request.json)


@app.route("/delTecnico", methods=["POST"])
def delTecnico():
    resultado = técnicoDAO.TécnicoDAO()
    return resultado.delTécnico(request.json)


"""
  Fim rota: Técnico
"""
"""
  Rotas do WebService para a classe: SendEmail
"""
import sendemail


@app.route("/sendEmail", methods=["POST"])
def SendEmail():
    resultado = sendemail.sendEmail()
    return resultado.Email(request.json)


"""
  Fim rota: SendEmail
"""

"""
  Rotas do WebService para a classe: Config (TB00040)
"""
import configDAO


@app.route("/listConfig/", methods=["POST"])
def listConfig():
    resultado = configDAO.ConfigDAO()
    return resultado.listConfig(request.json)


@app.route("/dictConfig/", methods=["POST"])
def dictConfig():
    resultado = configDAO.ConfigDAO()
    return resultado.dictConfig(request.json)


@app.route("/fieldsConfig/", methods=["POST"])
def fieldsConfig():
    resultado = configDAO.ConfigDAO()
    return resultado.fieldsConfig(request.json)


@app.route("/findConfig/", methods=["POST"])
def findConfig():
    resultado = configDAO.ConfigDAO()
    return resultado.findConfig(request.json)


"""
  Fim rota: Config
"""

"""
  Rotas do WebService para a classe: Documento (TB00110)
"""
import documentoDAO


@app.route("/listDocumento/", methods=["POST"])
def listDocumento():
    resultado = documentoDAO.DocumentoDAO()
    return resultado.listDocumento(request.json)


@app.route("/dictDocumento/", methods=["POST"])
def dictDocumento():
    resultado = documentoDAO.DocumentoDAO()
    return resultado.dictDocumento(request.json)


@app.route("/fieldsDocumento/", methods=["POST"])
def fieldsDocumento():
    resultado = documentoDAO.DocumentoDAO()
    return resultado.fieldsDocumento(request.json)


@app.route("/findDocumento/", methods=["POST"])
def findDocumento():
    resultado = documentoDAO.DocumentoDAO()
    return resultado.findDocumento(request.json)


@app.route("/DocumentoID", methods=["POST"])
def documentoID():
    resultado = documentoDAO.DocumentoDAO()
    return resultado.documentoID(request.json)


@app.route("/insDocumento", methods=["POST"])
def insDocumento():
    resultado = documentoDAO.DocumentoDAO()
    return resultado.insDocumento(request.json)


@app.route("/updDocumento", methods=["POST"])
def updDocumento():
    resultado = documentoDAO.DocumentoDAO()
    return resultado.updDocumento(request.json)


@app.route("/delDocumento", methods=["POST"])
def delDocumento():
    resultado = documentoDAO.DocumentoDAO()
    return resultado.delDocumento(request.json)


"""
  Fim rota: Documento
"""

"""
  Rotas do WebService para a classe: Email (TB00111)
"""
import emailDAO


@app.route("/listEmail/", methods=["POST"])
def listEmail():
    resultado = emailDAO.EmailDAO()
    return resultado.listEmail(request.json)


@app.route("/dictEmail/", methods=["POST"])
def dictEmail():
    resultado = emailDAO.EmailDAO()
    return resultado.dictEmail(request.json)


@app.route("/fieldsEmail/", methods=["POST"])
def fieldsEmail():
    resultado = emailDAO.EmailDAO()
    return resultado.fieldsEmail(request.json)


@app.route("/findEmail/", methods=["POST"])
def findEmail():
    resultado = emailDAO.EmailDAO()
    return resultado.findEmail(request.json)


@app.route("/EmailID", methods=["POST"])
def emailID():
    resultado = emailDAO.EmailDAO()
    return resultado.emailID(request.json)


@app.route("/insEmail", methods=["POST"])
def insEmail():
    resultado = emailDAO.EmailDAO()
    return resultado.insEmail(request.json)


@app.route("/updEmail", methods=["POST"])
def updEmail():
    resultado = emailDAO.EmailDAO()
    return resultado.updEmail(request.json)


@app.route("/delEmail", methods=["POST"])
def delEmail():
    resultado = emailDAO.EmailDAO()
    return resultado.delEmail(request.json)


"""
  Fim rota: Email
"""

"""
  Rotas do WebService para a classe: Attachment (TB00112)
"""
import attachmentDAO


@app.route("/listAttachment/", methods=["POST"])
def listAttachment():
    resultado = attachmentDAO.AttachmentDAO()
    return resultado.listAttachment(request.json)


@app.route("/dictAttachment/", methods=["POST"])
def dictAttachment():
    resultado = attachmentDAO.AttachmentDAO()
    return resultado.dictAttachment(request.json)


@app.route("/fieldsAttachment/", methods=["POST"])
def fieldsAttachment():
    resultado = attachmentDAO.AttachmentDAO()
    return resultado.fieldsAttachment(request.json)


@app.route("/findAttachment/", methods=["POST"])
def findAttachment():
    resultado = attachmentDAO.AttachmentDAO()
    return resultado.findAttachment(request.json)


@app.route("/AttachmentID", methods=["POST"])
def attachmentID():
    resultado = attachmentDAO.AttachmentDAO()
    return resultado.attachmentID(request.json)


@app.route("/insAttachment", methods=["POST"])
def insAttachment():
    resultado = attachmentDAO.AttachmentDAO()
    return resultado.insAttachment(request.json)


@app.route("/updAttachment", methods=["POST"])
def updAttachment():
    resultado = attachmentDAO.AttachmentDAO()
    return resultado.updAttachment(request.json)


@app.route("/delAttachment", methods=["POST"])
def delAttachment():
    resultado = attachmentDAO.AttachmentDAO()
    return resultado.delAttachment(request.json)


"""
  Fim rota: Attachment
"""

"""
  Rotas do WebService para a classe: PropostaModelo (TB01140)
"""
import propostamodeloDAO


@app.route("/listPropostaModelo/", methods=["POST"])
def listPropostaModelo():
    resultado = propostamodeloDAO.PropostaModeloDAO()
    return resultado.listPropostaModelo(request.json)


@app.route("/dictPropostaModelo/", methods=["POST"])
def dictPropostaModelo():
    resultado = propostamodeloDAO.PropostaModeloDAO()
    return resultado.dictPropostaModelo(request.json)


@app.route("/fieldsPropostaModelo/", methods=["POST"])
def fieldsPropostaModelo():
    resultado = propostamodeloDAO.PropostaModeloDAO()
    return resultado.fieldsPropostaModelo(request.json)


@app.route("/findPropostaModelo/", methods=["POST"])
def findPropostaModelo():
    resultado = propostamodeloDAO.PropostaModeloDAO()
    return resultado.findPropostaModelo(request.json)


@app.route("/PropostaModeloID", methods=["POST"])
def propostamodeloID():
    resultado = propostamodeloDAO.PropostaModeloDAO()
    return resultado.propostamodeloID(request.json)


@app.route("/insPropostaModelo", methods=["POST"])
def insPropostaModelo():
    resultado = propostamodeloDAO.PropostaModeloDAO()
    return resultado.insPropostaModelo(request.json)


@app.route("/updPropostaModelo", methods=["POST"])
def updPropostaModelo():
    resultado = propostamodeloDAO.PropostaModeloDAO()
    return resultado.updPropostaModelo(request.json)


@app.route("/delPropostaModelo", methods=["POST"])
def delPropostaModelo():
    resultado = propostamodeloDAO.PropostaModeloDAO()
    return resultado.delPropostaModelo(request.json)


"""
  Fim rota: PropostaModelo
"""

"""
  Rotas do WebService para a classe: PlaceHolder (TB01141)
"""
import placeholderDAO


@app.route("/listPlaceHolder/", methods=["POST"])
def listPlaceHolder():
    resultado = placeholderDAO.PlaceHolderDAO()
    return resultado.listPlaceHolder(request.json)


@app.route("/dictPlaceHolder/", methods=["POST"])
def dictPlaceHolder():
    resultado = placeholderDAO.PlaceHolderDAO()
    return resultado.dictPlaceHolder(request.json)


@app.route("/fieldsPlaceHolder/", methods=["POST"])
def fieldsPlaceHolder():
    resultado = placeholderDAO.PlaceHolderDAO()
    return resultado.fieldsPlaceHolder(request.json)


@app.route("/findPlaceHolder/", methods=["POST"])
def findPlaceHolder():
    resultado = placeholderDAO.PlaceHolderDAO()
    return resultado.findPlaceHolder(request.json)


@app.route("/PlaceHolderID", methods=["POST"])
def placeholderID():
    resultado = placeholderDAO.PlaceHolderDAO()
    return resultado.placeholderID(request.json)


@app.route("/insPlaceHolder", methods=["POST"])
def insPlaceHolder():
    resultado = placeholderDAO.PlaceHolderDAO()
    return resultado.insPlaceHolder(request.json)


@app.route("/updPlaceHolder", methods=["POST"])
def updPlaceHolder():
    resultado = placeholderDAO.PlaceHolderDAO()
    return resultado.updPlaceHolder(request.json)


@app.route("/delPlaceHolder", methods=["POST"])
def delPlaceHolder():
    resultado = placeholderDAO.PlaceHolderDAO()
    return resultado.delPlaceHolder(request.json)


"""
  Fim rota: PlaceHolder
"""

"""
  Rotas do WebService para a classe: TableVW (VW00018)
"""
import tablevwDAO


@app.route("/listTableVW/", methods=["POST"])
def listTableVW():
    resultado = tablevwDAO.TableVWDAO()
    return resultado.listTableVW(request.json)


@app.route("/dictTableVW/", methods=["POST"])
def dictTableVW():
    resultado = tablevwDAO.TableVWDAO()
    return resultado.dictTableVW(request.json)


@app.route("/fieldsTableVW/", methods=["POST"])
def fieldsTableVW():
    resultado = tablevwDAO.TableVWDAO()
    return resultado.fieldsTableVW(request.json)


"""
  Fim rota: TableVW
"""

"""
  Rotas do WebService para a classe: FieldVW (VW00019)
"""
import fieldvwDAO


@app.route("/listFieldVW/", methods=["POST"])
def listFieldVW():
    resultado = fieldvwDAO.FieldVWDAO()
    return resultado.listFieldVW(request.json)


@app.route("/dictFieldVW/", methods=["POST"])
def dictFieldVW():
    resultado = fieldvwDAO.FieldVWDAO()
    return resultado.dictFieldVW(request.json)


@app.route("/fieldsFieldVW/", methods=["POST"])
def fieldsFieldVW():
    resultado = fieldvwDAO.FieldVWDAO()
    return resultado.fieldsFieldVW(request.json)


@app.route("/findFieldVW/", methods=["POST"])
def findFieldVW():
    resultado = fieldvwDAO.FieldVWDAO()
    return resultado.findFieldVW(request.json)


"""
  Fim rota: FieldVW
"""

"""
  Rotas do WebService para a classe: Documento
"""
import documento


@app.route("/createDocument/", methods=["POST"])
def createDocument():
    resultado = documento.Documento()
    return resultado.createDocument(request.json)


@app.route("/convertDocument/", methods=["POST"])
def convertDocument():
    resultado = documento.Documento()
    return resultado.convertDocument(request.json)


@app.route("/converttoPDF/", methods=["POST"])
def converttoPDF():
    resultado = documento.Documento()
    return resultado.converttoPDF(request.json)


"""
  Fim rota: Documento
"""

"""
  Rotas do WebService para a classe: ContratoSite (TB02176)
"""
import contratositeDAO


@app.route("/listContratoSite/", methods=["POST"])
def listContratoSite():
    resultado = contratositeDAO.ContratoSiteDAO()
    return resultado.listContratoSite(request.json)


@app.route("/dictContratoSite/", methods=["POST"])
def dictContratoSite():
    resultado = contratositeDAO.ContratoSiteDAO()
    return resultado.dictContratoSite(request.json)


@app.route("/fieldsContratoSite/", methods=["POST"])
def fieldsContratoSite():
    resultado = contratositeDAO.ContratoSiteDAO()
    return resultado.fieldsContratoSite(request.json)


@app.route("/findContratoSite/", methods=["POST"])
def findContratoSite():
    resultado = contratositeDAO.ContratoSiteDAO()
    return resultado.findContratoSite(request.json)


@app.route("/ContratoSiteID", methods=["POST"])
def contratositeID():
    resultado = contratositeDAO.ContratoSiteDAO()
    return resultado.contratositeID(request.json)


@app.route("/insContratoSite", methods=["POST"])
def insContratoSite():
    resultado = contratositeDAO.ContratoSiteDAO()
    return resultado.insContratoSite(request.json)


@app.route("/updContratoSite", methods=["POST"])
def updContratoSite():
    resultado = contratositeDAO.ContratoSiteDAO()
    return resultado.updContratoSite(request.json)


@app.route("/delContratoSite", methods=["POST"])
def delContratoSite():
    resultado = contratositeDAO.ContratoSiteDAO()
    return resultado.delContratoSite(request.json)


"""
  Fim rota: ContratoSite
"""

"""
  Rotas do WebService para a classe: ContratoDepto (TB02177)
"""
import contratodeptoDAO


@app.route("/listContratoDepto/", methods=["POST"])
def listContratoDepto():
    resultado = contratodeptoDAO.ContratoDeptoDAO()
    return resultado.listContratoDepto(request.json)


@app.route("/dictContratoDepto/", methods=["POST"])
def dictContratoDepto():
    resultado = contratodeptoDAO.ContratoDeptoDAO()
    return resultado.dictContratoDepto(request.json)


@app.route("/fieldsContratoDepto/", methods=["POST"])
def fieldsContratoDepto():
    resultado = contratodeptoDAO.ContratoDeptoDAO()
    return resultado.fieldsContratoDepto(request.json)


@app.route("/findContratoDepto/", methods=["POST"])
def findContratoDepto():
    resultado = contratodeptoDAO.ContratoDeptoDAO()
    return resultado.findContratoDepto(request.json)


@app.route("/ContratoDeptoID", methods=["POST"])
def contratodeptoID():
    resultado = contratodeptoDAO.ContratoDeptoDAO()
    return resultado.contratodeptoID(request.json)


@app.route("/insContratoDepto", methods=["POST"])
def insContratoDepto():
    resultado = contratodeptoDAO.ContratoDeptoDAO()
    return resultado.insContratoDepto(request.json)


@app.route("/updContratoDepto", methods=["POST"])
def updContratoDepto():
    resultado = contratodeptoDAO.ContratoDeptoDAO()
    return resultado.updContratoDepto(request.json)


@app.route("/delContratoDepto", methods=["POST"])
def delContratoDepto():
    resultado = contratodeptoDAO.ContratoDeptoDAO()
    return resultado.delContratoDepto(request.json)


"""
  Fim rota: ContratoDepto
"""

"""
  Rotas do WebService para a classe: ContratoApuracao (TB02247)
"""
import contratoapuracaoDAO


@app.route("/listContratoApuracao/", methods=["POST"])
def listContratoApuracao():
    resultado = contratoapuracaoDAO.ContratoApuracaoDAO()
    return resultado.listContratoApuracao(request.json)


@app.route("/dictContratoApuracao/", methods=["POST"])
def dictContratoApuracao():
    resultado = contratoapuracaoDAO.ContratoApuracaoDAO()
    return resultado.dictContratoApuracao(request.json)


@app.route("/fieldsContratoApuracao/", methods=["POST"])
def fieldsContratoApuracao():
    resultado = contratoapuracaoDAO.ContratoApuracaoDAO()
    return resultado.fieldsContratoApuracao(request.json)


@app.route("/findContratoApuracao/", methods=["POST"])
def findContratoApuracao():
    resultado = contratoapuracaoDAO.ContratoApuracaoDAO()
    return resultado.findContratoApuracao(request.json)


@app.route("/ContratoApuracaoID", methods=["POST"])
def contratoapuracaoID():
    resultado = contratoapuracaoDAO.ContratoApuracaoDAO()
    return resultado.contratoapuracaoID(request.json)


@app.route("/insContratoApuracao", methods=["POST"])
def insContratoApuracao():
    resultado = contratoapuracaoDAO.ContratoApuracaoDAO()
    return resultado.insContratoApuracao(request.json)


@app.route("/updContratoApuracao", methods=["POST"])
def updContratoApuracao():
    resultado = contratoapuracaoDAO.ContratoApuracaoDAO()
    return resultado.updContratoApuracao(request.json)


@app.route("/delContratoApuracao", methods=["POST"])
def delContratoApuracao():
    resultado = contratoapuracaoDAO.ContratoApuracaoDAO()
    return resultado.delContratoApuracao(request.json)


"""
  Fim rota: ContratoApuracao
"""

"""
  Rotas do WebService para a classe: ContratoApuracaoVW (VW02285)
"""
import contratoapuracaovwDAO


@app.route("/listContratoApuracaoVW/", methods=["POST"])
def listContratoApuracaoVW():
    resultado = contratoapuracaovwDAO.ContratoApuracaoVWDAO()
    return resultado.listContratoApuracaoVW(request.json)


@app.route("/dictContratoApuracaoVW/", methods=["POST"])
def dictContratoApuracaoVW():
    resultado = contratoapuracaovwDAO.ContratoApuracaoVWDAO()
    return resultado.dictContratoApuracaoVW(request.json)


@app.route("/fieldsContratoApuracaoVW/", methods=["POST"])
def fieldsContratoApuracaoVW():
    resultado = contratoapuracaovwDAO.ContratoApuracaoVWDAO()
    return resultado.fieldsContratoApuracaoVW(request.json)


@app.route("/findContratoApuracaoVW/", methods=["POST"])
def findContratoApuracaoVW():
    resultado = contratoapuracaovwDAO.ContratoApuracaoVWDAO()
    return resultado.findContratoApuracaoVW(request.json)


"""
  Fim rota: ContratoApuracaoVW
"""

"""
  Rotas do WebService para a classe: ContratoItem (TB02274)
"""
import contratoitemDAO


@app.route("/listContratoItem/", methods=["POST"])
def listContratoItem():
    resultado = contratoitemDAO.ContratoItemDAO()
    return resultado.listContratoItem(request.json)


@app.route("/dictContratoItem/", methods=["POST"])
def dictContratoItem():
    resultado = contratoitemDAO.ContratoItemDAO()
    return resultado.dictContratoItem(request.json)


@app.route("/fieldsContratoItem/", methods=["POST"])
def fieldsContratoItem():
    resultado = contratoitemDAO.ContratoItemDAO()
    return resultado.fieldsContratoItem(request.json)


@app.route("/findContratoItem/", methods=["POST"])
def findContratoItem():
    resultado = contratoitemDAO.ContratoItemDAO()
    return resultado.findContratoItem(request.json)


@app.route("/ContratoItemID", methods=["POST"])
def contratoitemID():
    resultado = contratoitemDAO.ContratoItemDAO()
    return resultado.contratoitemID(request.json)


@app.route("/insContratoItem", methods=["POST"])
def insContratoItem():
    resultado = contratoitemDAO.ContratoItemDAO()
    return resultado.insContratoItem(request.json)


@app.route("/updContratoItem", methods=["POST"])
def updContratoItem():
    resultado = contratoitemDAO.ContratoItemDAO()
    return resultado.updContratoItem(request.json)


@app.route("/delContratoItem", methods=["POST"])
def delContratoItem():
    resultado = contratoitemDAO.ContratoItemDAO()
    return resultado.delContratoItem(request.json)


"""
  Fim rota: ContratoItem
"""

"""
  Rotas do WebService para a classe: ContratoTotal (TB02275)
"""
import contratototalDAO


@app.route("/listContratoTotal/", methods=["POST"])
def listContratoTotal():
    resultado = contratototalDAO.ContratoTotalDAO()
    return resultado.listContratoTotal(request.json)


@app.route("/dictContratoTotal/", methods=["POST"])
def dictContratoTotal():
    resultado = contratototalDAO.ContratoTotalDAO()
    return resultado.dictContratoTotal(request.json)


@app.route("/fieldsContratoTotal/", methods=["POST"])
def fieldsContratoTotal():
    resultado = contratototalDAO.ContratoTotalDAO()
    return resultado.fieldsContratoTotal(request.json)


@app.route("/findContratoTotal/", methods=["POST"])
def findContratoTotal():
    resultado = contratototalDAO.ContratoTotalDAO()
    return resultado.findContratoTotal(request.json)


@app.route("/ContratoTotalID", methods=["POST"])
def contratototalID():
    resultado = contratototalDAO.ContratoTotalDAO()
    return resultado.contratototalID(request.json)


@app.route("/insContratoTotal", methods=["POST"])
def insContratoTotal():
    resultado = contratototalDAO.ContratoTotalDAO()
    return resultado.insContratoTotal(request.json)


@app.route("/updContratoTotal", methods=["POST"])
def updContratoTotal():
    resultado = contratototalDAO.ContratoTotalDAO()
    return resultado.updContratoTotal(request.json)


@app.route("/delContratoTotal", methods=["POST"])
def delContratoTotal():
    resultado = contratototalDAO.ContratoTotalDAO()
    return resultado.delContratoTotal(request.json)


"""
  Fim rota: ContratoTotal
"""

"""
  Rotas do WebService para a classe: ContratoItemVW (VW02287)
"""
import contratoitemvwDAO


@app.route("/listContratoItemVW/", methods=["POST"])
def listContratoItemVW():
    resultado = contratoitemvwDAO.ContratoItemVWDAO()
    return resultado.listContratoItemVW(request.json)


@app.route("/dictContratoItemVW/", methods=["POST"])
def dictContratoItemVW():
    resultado = contratoitemvwDAO.ContratoItemVWDAO()
    return resultado.dictContratoItemVW(request.json)


@app.route("/fieldsContratoItemVW/", methods=["POST"])
def fieldsContratoItemVW():
    resultado = contratoitemvwDAO.ContratoItemVWDAO()
    return resultado.fieldsContratoItemVW(request.json)


@app.route("/findContratoItemVW/", methods=["POST"])
def findContratoItemVW():
    resultado = contratoitemvwDAO.ContratoItemVWDAO()
    return resultado.findContratoItemVW(request.json)


"""
  Fim rota: ContratoItemVW
"""

"""
  Rotas do WebService para a classe: ContratoComissao (TB02155)
"""
import contratocomissaoDAO


@app.route("/listContratoComissao/", methods=["POST"])
def listContratoComissao():
    resultado = contratocomissaoDAO.ContratoComissaoDAO()
    return resultado.listContratoComissao(request.json)


@app.route("/dictContratoComissao/", methods=["POST"])
def dictContratoComissao():
    resultado = contratocomissaoDAO.ContratoComissaoDAO()
    return resultado.dictContratoComissao(request.json)


@app.route("/fieldsContratoComissao/", methods=["POST"])
def fieldsContratoComissao():
    resultado = contratocomissaoDAO.ContratoComissaoDAO()
    return resultado.fieldsContratoComissao(request.json)


@app.route("/findContratoComissao/", methods=["POST"])
def findContratoComissao():
    resultado = contratocomissaoDAO.ContratoComissaoDAO()
    return resultado.findContratoComissao(request.json)


@app.route("/ContratoComissaoID", methods=["POST"])
def contratocomissaoID():
    resultado = contratocomissaoDAO.ContratoComissaoDAO()
    return resultado.contratocomissaoID(request.json)


@app.route("/insContratoComissao", methods=["POST"])
def insContratoComissao():
    resultado = contratocomissaoDAO.ContratoComissaoDAO()
    return resultado.insContratoComissao(request.json)


@app.route("/updContratoComissao", methods=["POST"])
def updContratoComissao():
    resultado = contratocomissaoDAO.ContratoComissaoDAO()
    return resultado.updContratoComissao(request.json)


@app.route("/delContratoComissao", methods=["POST"])
def delContratoComissao():
    resultado = contratocomissaoDAO.ContratoComissaoDAO()
    return resultado.delContratoComissao(request.json)


"""
  Fim rota: ContratoComissao
"""

"""
  Rotas do WebService para a classe: ContratoComissaoVW (VW02155)
"""
import contratocomissaovwDAO


@app.route("/listContratoComissaoVW/", methods=["POST"])
def listContratoComissaoVW():
    resultado = contratocomissaovwDAO.ContratoComissaoVWDAO()
    return resultado.listContratoComissaoVW(request.json)


@app.route("/dictContratoComissaoVW/", methods=["POST"])
def dictContratoComissaoVW():
    resultado = contratocomissaovwDAO.ContratoComissaoVWDAO()
    return resultado.dictContratoComissaoVW(request.json)


@app.route("/fieldsContratoComissaoVW/", methods=["POST"])
def fieldsContratoComissaoVW():
    resultado = contratocomissaovwDAO.ContratoComissaoVWDAO()
    return resultado.fieldsContratoComissaoVW(request.json)


@app.route("/findContratoComissaoVW/", methods=["POST"])
def findContratoComissaoVW():
    resultado = contratocomissaovwDAO.ContratoComissaoVWDAO()
    return resultado.findContratoComissaoVW(request.json)


"""
  Fim rota: ContratoComissaoVW
"""

"""
  Rotas do WebService para a classe: Contrato (TB02111)
"""
import contratoDAO


@app.route("/listContrato/", methods=["POST"])
def listContrato():
    resultado = contratoDAO.ContratoDAO()
    return resultado.listContrato(request.json)


@app.route("/dictContrato/", methods=["POST"])
def dictContrato():
    resultado = contratoDAO.ContratoDAO()
    return resultado.dictContrato(request.json)


@app.route("/fieldsContrato/", methods=["POST"])
def fieldsContrato():
    resultado = contratoDAO.ContratoDAO()
    return resultado.fieldsContrato(request.json)


@app.route("/findContrato/", methods=["POST"])
def findContrato():
    resultado = contratoDAO.ContratoDAO()
    return resultado.findContrato(request.json)


@app.route("/insContrato", methods=["POST"])
def insContrato():
    resultado = contratoDAO.ContratoDAO()
    return resultado.insContrato(request.json)


@app.route("/updContrato", methods=["POST"])
def updContrato():
    resultado = contratoDAO.ContratoDAO()
    return resultado.updContrato(request.json)


@app.route("/delContrato", methods=["POST"])
def delContrato():
    resultado = contratoDAO.ContratoDAO()
    return resultado.delContrato(request.json)


"""
  Fim rota: Contrato
"""

"""
  Rotas do WebService para a classe: ContratoVW (VW02091)
"""
import contratovwDAO


@app.route("/listContratoVW/", methods=["POST"])
def listContratoVW():
    resultado = contratovwDAO.ContratoVWDAO()
    return resultado.listContratoVW(request.json)


@app.route("/dictContratoVW/", methods=["POST"])
def dictContratoVW():
    resultado = contratovwDAO.ContratoVWDAO()
    return resultado.dictContratoVW(request.json)


@app.route("/fieldsContratoVW/", methods=["POST"])
def fieldsContratoVW():
    resultado = contratovwDAO.ContratoVWDAO()
    return resultado.fieldsContratoVW(request.json)


@app.route("/findContratoVW/", methods=["POST"])
def findContratoVW():
    resultado = contratovwDAO.ContratoVWDAO()
    return resultado.findContratoVW(request.json)


"""
  Fim rota: ContratoVW
"""

"""
  Rotas do WebService para a classe: OportunidadeNotificacao (TB01143)
"""
import oportunidadenotificacaoDAO


@app.route("/listOportunidadeNotificacao/", methods=["POST"])
def listOportunidadeNotificacao():
    resultado = oportunidadenotificacaoDAO.OportunidadeNotificacaoDAO()
    return resultado.listOportunidadeNotificacao(request.json)


@app.route("/dictOportunidadeNotificacao/", methods=["POST"])
def dictOportunidadeNotificacao():
    resultado = oportunidadenotificacaoDAO.OportunidadeNotificacaoDAO()
    return resultado.dictOportunidadeNotificacao(request.json)


@app.route("/fieldsOportunidadeNotificacao/", methods=["POST"])
def fieldsOportunidadeNotificacao():
    resultado = oportunidadenotificacaoDAO.OportunidadeNotificacaoDAO()
    return resultado.fieldsOportunidadeNotificacao(request.json)


@app.route("/findOportunidadeNotificacao/", methods=["POST"])
def findOportunidadeNotificacao():
    resultado = oportunidadenotificacaoDAO.OportunidadeNotificacaoDAO()
    return resultado.findOportunidadeNotificacao(request.json)


@app.route("/insOportunidadeNotificacao", methods=["POST"])
def insOportunidadeNotificacao():
    resultado = oportunidadenotificacaoDAO.OportunidadeNotificacaoDAO()
    return resultado.insOportunidadeNotificacao(request.json)


@app.route("/updOportunidadeNotificacao", methods=["POST"])
def updOportunidadeNotificacao():
    resultado = oportunidadenotificacaoDAO.OportunidadeNotificacaoDAO()
    return resultado.updOportunidadeNotificacao(request.json)


@app.route("/delOportunidadeNotificacao", methods=["POST"])
def delOportunidadeNotificacao():
    resultado = oportunidadenotificacaoDAO.OportunidadeNotificacaoDAO()
    return resultado.delOportunidadeNotificacao(request.json)


"""
  Fim rota: OportunidadeNotificacao
"""

"""
  Rotas do WebService para a classe: PrecontratoNotificacao (TB01144)
"""
import precontratonotificacaoDAO


@app.route("/listPrecontratoNotificacao/", methods=["POST"])
def listPrecontratoNotificacao():
    resultado = precontratonotificacaoDAO.PrecontratoNotificacaoDAO()
    return resultado.listPrecontratoNotificacao(request.json)


@app.route("/dictPrecontratoNotificacao/", methods=["POST"])
def dictPrecontratoNotificacao():
    resultado = precontratonotificacaoDAO.PrecontratoNotificacaoDAO()
    return resultado.dictPrecontratoNotificacao(request.json)


@app.route("/fieldsPrecontratoNotificacao/", methods=["POST"])
def fieldsPrecontratoNotificacao():
    resultado = precontratonotificacaoDAO.PrecontratoNotificacaoDAO()
    return resultado.fieldsPrecontratoNotificacao(request.json)


@app.route("/findPrecontratoNotificacao/", methods=["POST"])
def findPrecontratoNotificacao():
    resultado = precontratonotificacaoDAO.PrecontratoNotificacaoDAO()
    return resultado.findPrecontratoNotificacao(request.json)


@app.route("/insPrecontratoNotificacao", methods=["POST"])
def insPrecontratoNotificacao():
    resultado = precontratonotificacaoDAO.PrecontratoNotificacaoDAO()
    return resultado.insPrecontratoNotificacao(request.json)


@app.route("/updPrecontratoNotificacao", methods=["POST"])
def updPrecontratoNotificacao():
    resultado = precontratonotificacaoDAO.PrecontratoNotificacaoDAO()
    return resultado.updPrecontratoNotificacao(request.json)


@app.route("/delPrecontratoNotificacao", methods=["POST"])
def delPrecontratoNotificacao():
    resultado = precontratonotificacaoDAO.PrecontratoNotificacaoDAO()
    return resultado.delPrecontratoNotificacao(request.json)


"""
  Fim rota: PrecontratoNotificacao
"""

"""
  Rotas do WebService para a classe: ContratoFaturaVW (VW02193)
"""
import contratofaturavwDAO


@app.route("/listContratoFaturaVW/", methods=["POST"])
def listContratoFaturaVW():
    resultado = contratofaturavwDAO.ContratoFaturaVWDAO()
    return resultado.listContratoFaturaVW(request.json)


@app.route("/dictContratoFaturaVW/", methods=["POST"])
def dictContratoFaturaVW():
    resultado = contratofaturavwDAO.ContratoFaturaVWDAO()
    return resultado.dictContratoFaturaVW(request.json)


@app.route("/fieldsContratoFaturaVW/", methods=["POST"])
def fieldsContratoFaturaVW():
    resultado = contratofaturavwDAO.ContratoFaturaVWDAO()
    return resultado.fieldsContratoFaturaVW(request.json)


@app.route("/findContratoFaturaVW/", methods=["POST"])
def findContratoFaturaVW():
    resultado = contratofaturavwDAO.ContratoFaturaVWDAO()
    return resultado.findContratoFaturaVW(request.json)


"""
  Fim rota: ContratoFaturaVW
"""

"""
  Rotas do WebService para a classe: ReceberVW (VW04004)
"""
import recebervwDAO


@app.route("/listReceberVW/", methods=["POST"])
def listReceberVW():
    resultado = recebervwDAO.ReceberVWDAO()
    return resultado.listReceberVW(request.json)


@app.route("/dictReceberVW/", methods=["POST"])
def dictReceberVW():
    resultado = recebervwDAO.ReceberVWDAO()
    return resultado.dictReceberVW(request.json)


@app.route("/fieldsReceberVW/", methods=["POST"])
def fieldsReceberVW():
    resultado = recebervwDAO.ReceberVWDAO()
    return resultado.fieldsReceberVW(request.json)


@app.route("/findReceberVW/", methods=["POST"])
def findReceberVW():
    resultado = recebervwDAO.ReceberVWDAO()
    return resultado.findReceberVW(request.json)


"""
  Fim rota: ReceberVW
"""

"""
  Rotas do WebService para a classe: GmoVW (VW02288)
"""
import gmovwDAO


@app.route("/listGmoVW/", methods=["POST"])
def listGmoVW():
    resultado = gmovwDAO.GmoVWDAO()
    return resultado.listGmoVW(request.json)


@app.route("/dictGmoVW/", methods=["POST"])
def dictGmoVW():
    resultado = gmovwDAO.GmoVWDAO()
    return resultado.dictGmoVW(request.json)


@app.route("/fieldsGmoVW/", methods=["POST"])
def fieldsGmoVW():
    resultado = gmovwDAO.GmoVWDAO()
    return resultado.fieldsGmoVW(request.json)


@app.route("/findGmoVW/", methods=["POST"])
def findGmoVW():
    resultado = gmovwDAO.GmoVWDAO()
    return resultado.findGmoVW(request.json)


"""
  Fim rota: GmoVW
"""

"""
  Rotas do WebService para a classe: GmoItemVW (VW02289)
"""
import gmoitemvwDAO


@app.route("/listGmoItemVW/", methods=["POST"])
def listGmoItemVW():
    resultado = gmoitemvwDAO.GmoItemVWDAO()
    return resultado.listGmoItemVW(request.json)


@app.route("/dictGmoItemVW/", methods=["POST"])
def dictGmoItemVW():
    resultado = gmoitemvwDAO.GmoItemVWDAO()
    return resultado.dictGmoItemVW(request.json)


@app.route("/fieldsGmoItemVW/", methods=["POST"])
def fieldsGmoItemVW():
    resultado = gmoitemvwDAO.GmoItemVWDAO()
    return resultado.fieldsGmoItemVW(request.json)


@app.route("/findGmoItemVW/", methods=["POST"])
def findGmoItemVW():
    resultado = gmoitemvwDAO.GmoItemVWDAO()
    return resultado.findGmoItemVW(request.json)


"""
  Fim rota: GmoItemVW
"""

"""
  Rotas do WebService para a classe: ContratoStatusVW (VW02290)
"""
import contratostatusvwDAO


@app.route("/listContratoStatusVW/", methods=["POST"])
def listContratoStatusVW():
    resultado = contratostatusvwDAO.ContratoStatusVWDAO()
    return resultado.listContratoStatusVW(request.json)


@app.route("/dictContratoStatusVW/", methods=["POST"])
def dictContratoStatusVW():
    resultado = contratostatusvwDAO.ContratoStatusVWDAO()
    return resultado.dictContratoStatusVW(request.json)


@app.route("/fieldsContratoStatusVW/", methods=["POST"])
def fieldsContratoStatusVW():
    resultado = contratostatusvwDAO.ContratoStatusVWDAO()
    return resultado.fieldsContratoStatusVW(request.json)


@app.route("/findContratoStatusVW/", methods=["POST"])
def findContratoStatusVW():
    resultado = contratostatusvwDAO.ContratoStatusVWDAO()
    return resultado.findContratoStatusVW(request.json)


"""
  Fim rota: ContratoStatusVW
"""

"""
  Rotas do WebService para a classe: GmoTotalVW (VW02291)
"""
import gmototalvwDAO


@app.route("/listGmoTotalVW/", methods=["POST"])
def listGmoTotalVW():
    resultado = gmototalvwDAO.GmoTotalVWDAO()
    return resultado.listGmoTotalVW(request.json)


@app.route("/dictGmoTotalVW/", methods=["POST"])
def dictGmoTotalVW():
    resultado = gmototalvwDAO.GmoTotalVWDAO()
    return resultado.dictGmoTotalVW(request.json)


@app.route("/fieldsGmoTotalVW/", methods=["POST"])
def fieldsGmoTotalVW():
    resultado = gmototalvwDAO.GmoTotalVWDAO()
    return resultado.fieldsGmoTotalVW(request.json)


@app.route("/findGmoTotalVW/", methods=["POST"])
def findGmoTotalVW():
    resultado = gmototalvwDAO.GmoTotalVWDAO()
    return resultado.findGmoTotalVW(request.json)


"""
  Fim rota: GmoTotalVW
"""

"""
  Rotas do WebService para a classe: Os (TB02115)
"""
import osDAO


@app.route("/listOs/", methods=["POST"])
def listOs():
    resultado = osDAO.OsDAO()
    return resultado.listOs(request.json)


@app.route("/dictOs/", methods=["POST"])
def dictOs():
    resultado = osDAO.OsDAO()
    return resultado.dictOs(request.json)


@app.route("/fieldsOs/", methods=["POST"])
def fieldsOs():
    resultado = osDAO.OsDAO()
    return resultado.fieldsOs(request.json)


@app.route("/findOs/", methods=["POST"])
def findOs():
    resultado = osDAO.OsDAO()
    return resultado.findOs(request.json)


@app.route("/OsID", methods=["POST"])
def osID():
    resultado = osDAO.OsDAO()
    return resultado.osID(request.json)


@app.route("/insOs", methods=["POST"])
def insOs():
    resultado = osDAO.OsDAO()
    return resultado.insOs(request.json)


@app.route("/updOs", methods=["POST"])
def updOs():
    resultado = osDAO.OsDAO()
    return resultado.updOs(request.json)


@app.route("/delOs", methods=["POST"])
def delOs():
    resultado = osDAO.OsDAO()
    return resultado.delOs(request.json)


"""
  Fim rota: Os
"""

"""
  Rotas do WebService para a classe: OsVW (VW02095)
"""
import osvwDAO


@app.route("/listOsVW/", methods=["POST"])
def listOsVW():
    resultado = osvwDAO.OsVWDAO()
    return resultado.listOsVW(request.json)


@app.route("/dictOsVW/", methods=["POST"])
def dictOsVW():
    resultado = osvwDAO.OsVWDAO()
    return resultado.dictOsVW(request.json)


@app.route("/fieldsOsVW/", methods=["POST"])
def fieldsOsVW():
    resultado = osvwDAO.OsVWDAO()
    return resultado.fieldsOsVW(request.json)


@app.route("/findOsVW/", methods=["POST"])
def findOsVW():
    resultado = osvwDAO.OsVWDAO()
    return resultado.findOsVW(request.json)


"""
  Fim rota: OsVW
"""

"""
  Rotas do WebService para a classe: OsCondicao (TB01055)
"""
import oscondicaoDAO


@app.route("/listOsCondicao/", methods=["POST"])
def listOsCondicao():
    resultado = oscondicaoDAO.OsCondicaoDAO()
    return resultado.listOsCondicao(request.json)


@app.route("/dictOsCondicao/", methods=["POST"])
def dictOsCondicao():
    resultado = oscondicaoDAO.OsCondicaoDAO()
    return resultado.dictOsCondicao(request.json)


@app.route("/fieldsOsCondicao/", methods=["POST"])
def fieldsOsCondicao():
    resultado = oscondicaoDAO.OsCondicaoDAO()
    return resultado.fieldsOsCondicao(request.json)


@app.route("/findOsCondicao/", methods=["POST"])
def findOsCondicao():
    resultado = oscondicaoDAO.OsCondicaoDAO()
    return resultado.findOsCondicao(request.json)


@app.route("/OsCondicaoID", methods=["POST"])
def oscondicaoID():
    resultado = oscondicaoDAO.OsCondicaoDAO()
    return resultado.oscondicaoID(request.json)


@app.route("/insOsCondicao", methods=["POST"])
def insOsCondicao():
    resultado = oscondicaoDAO.OsCondicaoDAO()
    return resultado.insOsCondicao(request.json)


@app.route("/updOsCondicao", methods=["POST"])
def updOsCondicao():
    resultado = oscondicaoDAO.OsCondicaoDAO()
    return resultado.updOsCondicao(request.json)


@app.route("/delOsCondicao", methods=["POST"])
def delOsCondicao():
    resultado = oscondicaoDAO.OsCondicaoDAO()
    return resultado.delOsCondicao(request.json)


"""
  Fim rota: OsCondicao
"""

"""
  Rotas do WebService para a classe: OsStatus (TB01073)
"""
import osstatusDAO


@app.route("/listOsStatus/", methods=["POST"])
def listOsStatus():
    resultado = osstatusDAO.OsStatusDAO()
    return resultado.listOsStatus(request.json)


@app.route("/dictOsStatus/", methods=["POST"])
def dictOsStatus():
    resultado = osstatusDAO.OsStatusDAO()
    return resultado.dictOsStatus(request.json)


@app.route("/fieldsOsStatus/", methods=["POST"])
def fieldsOsStatus():
    resultado = osstatusDAO.OsStatusDAO()
    return resultado.fieldsOsStatus(request.json)


@app.route("/findOsStatus/", methods=["POST"])
def findOsStatus():
    resultado = osstatusDAO.OsStatusDAO()
    return resultado.findOsStatus(request.json)


@app.route("/OsStatusID", methods=["POST"])
def osstatusID():
    resultado = osstatusDAO.OsStatusDAO()
    return resultado.osstatusID(request.json)


@app.route("/insOsStatus", methods=["POST"])
def insOsStatus():
    resultado = osstatusDAO.OsStatusDAO()
    return resultado.insOsStatus(request.json)


@app.route("/updOsStatus", methods=["POST"])
def updOsStatus():
    resultado = osstatusDAO.OsStatusDAO()
    return resultado.updOsStatus(request.json)


@app.route("/delOsStatus", methods=["POST"])
def delOsStatus():
    resultado = osstatusDAO.OsStatusDAO()
    return resultado.delOsStatus(request.json)


"""
  Fim rota: OsStatus
"""

"""
  Rotas do WebService para a classe: OperacaoVenda (TB01022)
"""
import operacaovendaDAO


@app.route("/listOperacaoVenda/", methods=["POST"])
def listOperacaoVenda():
    resultado = operacaovendaDAO.OperacaoVendaDAO()
    return resultado.listOperacaoVenda(request.json)


@app.route("/dictOperacaoVenda/", methods=["POST"])
def dictOperacaoVenda():
    resultado = operacaovendaDAO.OperacaoVendaDAO()
    return resultado.dictOperacaoVenda(request.json)


@app.route("/fieldsOperacaoVenda/", methods=["POST"])
def fieldsOperacaoVenda():
    resultado = operacaovendaDAO.OperacaoVendaDAO()
    return resultado.fieldsOperacaoVenda(request.json)


@app.route("/findOperacaoVenda/", methods=["POST"])
def findOperacaoVenda():
    resultado = operacaovendaDAO.OperacaoVendaDAO()
    return resultado.findOperacaoVenda(request.json)


@app.route("/OperacaoVendaID", methods=["POST"])
def operacaovendaID():
    resultado = operacaovendaDAO.OperacaoVendaDAO()
    return resultado.operacaovendaID(request.json)


@app.route("/insOperacaoVenda", methods=["POST"])
def insOperacaoVenda():
    resultado = operacaovendaDAO.OperacaoVendaDAO()
    return resultado.insOperacaoVenda(request.json)


@app.route("/updOperacaoVenda", methods=["POST"])
def updOperacaoVenda():
    resultado = operacaovendaDAO.OperacaoVendaDAO()
    return resultado.updOperacaoVenda(request.json)


@app.route("/delOperacaoVenda", methods=["POST"])
def delOperacaoVenda():
    resultado = operacaovendaDAO.OperacaoVendaDAO()
    return resultado.delOperacaoVenda(request.json)


"""
  Fim rota: OperacaoVenda
"""

"""
  Rotas do WebService para a classe: CFOP (TB01011)
"""
import cfopDAO


@app.route("/listCFOP/", methods=["POST"])
def listCFOP():
    resultado = cfopDAO.CFOPDAO()
    return resultado.listCFOP(request.json)


@app.route("/dictCFOP/", methods=["POST"])
def dictCFOP():
    resultado = cfopDAO.CFOPDAO()
    return resultado.dictCFOP(request.json)


@app.route("/fieldsCFOP/", methods=["POST"])
def fieldsCFOP():
    resultado = cfopDAO.CFOPDAO()
    return resultado.fieldsCFOP(request.json)


@app.route("/findCFOP/", methods=["POST"])
def findCFOP():
    resultado = cfopDAO.CFOPDAO()
    return resultado.findCFOP(request.json)


@app.route("/CFOPID", methods=["POST"])
def cfopID():
    resultado = cfopDAO.CFOPDAO()
    return resultado.cfopID(request.json)


@app.route("/insCFOP", methods=["POST"])
def insCFOP():
    resultado = cfopDAO.CFOPDAO()
    return resultado.insCFOP(request.json)


@app.route("/updCFOP", methods=["POST"])
def updCFOP():
    resultado = cfopDAO.CFOPDAO()
    return resultado.updCFOP(request.json)


@app.route("/delCFOP", methods=["POST"])
def delCFOP():
    resultado = cfopDAO.CFOPDAO()
    return resultado.delCFOP(request.json)


"""
  Fim rota: CFOP
"""

"""
  Rotas do WebService para a classe: EstoqueVW (VW02001)
"""
import estoquevwDAO


@app.route("/listEstoqueVW/", methods=["POST"])
def listEstoqueVW():
    resultado = estoquevwDAO.EstoqueVWDAO()
    return resultado.listEstoqueVW(request.json)


@app.route("/dictEstoqueVW/", methods=["POST"])
def dictEstoqueVW():
    resultado = estoquevwDAO.EstoqueVWDAO()
    return resultado.dictEstoqueVW(request.json)


@app.route("/fieldsEstoqueVW/", methods=["POST"])
def fieldsEstoqueVW():
    resultado = estoquevwDAO.EstoqueVWDAO()
    return resultado.fieldsEstoqueVW(request.json)


@app.route("/findEstoqueVW/", methods=["POST"])
def findEstoqueVW():
    resultado = estoquevwDAO.EstoqueVWDAO()
    return resultado.findEstoqueVW(request.json)


"""
  Fim rota: EstoqueVW
"""

"""
  Rotas do WebService para a classe: SerialVW (VW02206)
"""
import serialvwDAO


@app.route("/listSerialVW/", methods=["POST"])
def listSerialVW():
    resultado = serialvwDAO.SerialVWDAO()
    return resultado.listSerialVW(request.json)


@app.route("/dictSerialVW/", methods=["POST"])
def dictSerialVW():
    resultado = serialvwDAO.SerialVWDAO()
    return resultado.dictSerialVW(request.json)


@app.route("/fieldsSerialVW/", methods=["POST"])
def fieldsSerialVW():
    resultado = serialvwDAO.SerialVWDAO()
    return resultado.fieldsSerialVW(request.json)


@app.route("/findSerialVW/", methods=["POST"])
def findSerialVW():
    resultado = serialvwDAO.SerialVWDAO()
    return resultado.findSerialVW(request.json)


"""
  Fim rota: SerialVW
"""

"""
  Rotas do WebService para a classe: DatawhatsChat (TB08014)
"""
import datawhatschatDAO


@app.route("/listDatawhatsChat/", methods=["POST"])
def listDatawhatsChat():
    resultado = datawhatschatDAO.DatawhatsChatDAO()
    return resultado.listDatawhatsChat(request.json)


@app.route("/dictDatawhatsChat/", methods=["POST"])
def dictDatawhatsChat():
    resultado = datawhatschatDAO.DatawhatsChatDAO()
    return resultado.dictDatawhatsChat(request.json)


@app.route("/fieldsDatawhatsChat/", methods=["POST"])
def fieldsDatawhatsChat():
    resultado = datawhatschatDAO.DatawhatsChatDAO()
    return resultado.fieldsDatawhatsChat(request.json)


@app.route("/findDatawhatsChat/", methods=["POST"])
def findDatawhatsChat():
    resultado = datawhatschatDAO.DatawhatsChatDAO()
    return resultado.findDatawhatsChat(request.json)


@app.route("/insDatawhatsChat", methods=["POST"])
def insDatawhatsChat():
    resultado = datawhatschatDAO.DatawhatsChatDAO()
    return resultado.insDatawhatsChat(request.json)


@app.route("/updDatawhatsChat", methods=["POST"])
def updDatawhatsChat():
    resultado = datawhatschatDAO.DatawhatsChatDAO()
    return resultado.updDatawhatsChat(request.json)


@app.route("/delDatawhatsChat", methods=["POST"])
def delDatawhatsChat():
    resultado = datawhatschatDAO.DatawhatsChatDAO()
    return resultado.delDatawhatsChat(request.json)


"""
  Fim rota: DatawhatsChat
"""

"""
  Rotas do WebService para a classe: DatawhatsFila (TB08021)
"""
import datawhatsfilaDAO


@app.route("/listDatawhatsFila/", methods=["POST"])
def listDatawhatsFila():
    resultado = datawhatsfilaDAO.DatawhatsFilaDAO()
    return resultado.listDatawhatsFila(request.json)


@app.route("/dictDatawhatsFila/", methods=["POST"])
def dictDatawhatsFila():
    resultado = datawhatsfilaDAO.DatawhatsFilaDAO()
    return resultado.dictDatawhatsFila(request.json)


@app.route("/fieldsDatawhatsFila/", methods=["POST"])
def fieldsDatawhatsFila():
    resultado = datawhatsfilaDAO.DatawhatsFilaDAO()
    return resultado.fieldsDatawhatsFila(request.json)


@app.route("/findDatawhatsFila/", methods=["POST"])
def findDatawhatsFila():
    resultado = datawhatsfilaDAO.DatawhatsFilaDAO()
    return resultado.findDatawhatsFila(request.json)


@app.route("/insDatawhatsFila", methods=["POST"])
def insDatawhatsFila():
    resultado = datawhatsfilaDAO.DatawhatsFilaDAO()
    return resultado.insDatawhatsFila(request.json)


@app.route("/updDatawhatsFila", methods=["POST"])
def updDatawhatsFila():
    resultado = datawhatsfilaDAO.DatawhatsFilaDAO()
    return resultado.updDatawhatsFila(request.json)


@app.route("/delDatawhatsFila", methods=["POST"])
def delDatawhatsFila():
    resultado = datawhatsfilaDAO.DatawhatsFilaDAO()
    return resultado.delDatawhatsFila(request.json)


"""
  Fim rota: DatawhatsFila
"""

"""
  Rotas do WebService para a classe: DatawhatsTalk (TB08026)
"""
import datawhatstalkDAO


@app.route("/listDatawhatsTalk/", methods=["POST"])
def listDatawhatsTalk():
    resultado = datawhatstalkDAO.DatawhatsTalkDAO()
    return resultado.listDatawhatsTalk(request.json)


@app.route("/dictDatawhatsTalk/", methods=["POST"])
def dictDatawhatsTalk():
    resultado = datawhatstalkDAO.DatawhatsTalkDAO()
    return resultado.dictDatawhatsTalk(request.json)


@app.route("/fieldsDatawhatsTalk/", methods=["POST"])
def fieldsDatawhatsTalk():
    resultado = datawhatstalkDAO.DatawhatsTalkDAO()
    return resultado.fieldsDatawhatsTalk(request.json)


@app.route("/findDatawhatsTalk/", methods=["POST"])
def findDatawhatsTalk():
    resultado = datawhatstalkDAO.DatawhatsTalkDAO()
    return resultado.findDatawhatsTalk(request.json)


@app.route("/insDatawhatsTalk", methods=["POST"])
def insDatawhatsTalk():
    resultado = datawhatstalkDAO.DatawhatsTalkDAO()
    return resultado.insDatawhatsTalk(request.json)


@app.route("/updDatawhatsTalk", methods=["POST"])
def updDatawhatsTalk():
    resultado = datawhatstalkDAO.DatawhatsTalkDAO()
    return resultado.updDatawhatsTalk(request.json)


@app.route("/delDatawhatsTalk", methods=["POST"])
def delDatawhatsTalk():
    resultado = datawhatstalkDAO.DatawhatsTalkDAO()
    return resultado.delDatawhatsTalk(request.json)


"""
  Fim rota: DatawhatsTalk
"""

"""
  Rotas do WebService para a classe: DatawhatsTalkVW (VW08013)
"""
import datawhatstalkvwDAO


@app.route("/listDatawhatsTalkVW/", methods=["POST"])
def listDatawhatsTalkVW():
    resultado = datawhatstalkvwDAO.DatawhatsTalkVWDAO()
    return resultado.listDatawhatsTalkVW(request.json)


@app.route("/dictDatawhatsTalkVW/", methods=["POST"])
def dictDatawhatsTalkVW():
    resultado = datawhatstalkvwDAO.DatawhatsTalkVWDAO()
    return resultado.dictDatawhatsTalkVW(request.json)


@app.route("/fieldsDatawhatsTalkVW/", methods=["POST"])
def fieldsDatawhatsTalkVW():
    resultado = datawhatstalkvwDAO.DatawhatsTalkVWDAO()
    return resultado.fieldsDatawhatsTalkVW(request.json)


@app.route("/findDatawhatsTalkVW/", methods=["POST"])
def findDatawhatsTalkVW():
    resultado = datawhatstalkvwDAO.DatawhatsTalkVWDAO()
    return resultado.findDatawhatsTalkVW(request.json)


"""
  Fim rota: DatawhatsTalkVW
"""

"""
  Rotas do WebService para a classe: DatawhatsChatVW (VW08014)
"""
import datawhatschatvwDAO


@app.route("/listDatawhatsChatVW/", methods=["POST"])
def listDatawhatsChatVW():
    resultado = datawhatschatvwDAO.DatawhatsChatVWDAO()
    return resultado.listDatawhatsChatVW(request.json)


@app.route("/dictDatawhatsChatVW/", methods=["POST"])
def dictDatawhatsChatVW():
    resultado = datawhatschatvwDAO.DatawhatsChatVWDAO()
    return resultado.dictDatawhatsChatVW(request.json)


@app.route("/fieldsDatawhatsChatVW/", methods=["POST"])
def fieldsDatawhatsChatVW():
    resultado = datawhatschatvwDAO.DatawhatsChatVWDAO()
    return resultado.fieldsDatawhatsChatVW(request.json)


@app.route("/findDatawhatsChatVW/", methods=["POST"])
def findDatawhatsChatVW():
    resultado = datawhatschatvwDAO.DatawhatsChatVWDAO()
    return resultado.findDatawhatsChatVW(request.json)


"""
  Fim rota: DatawhatsChatVW
"""

"""
  Rotas do WebService para a classe: DataWhatsCadchatVW (VW08005)
"""
import datawhatscadchatvwDAO


@app.route("/listDataWhatsCadchatVW/", methods=["POST"])
def listDataWhatsCadchatVW():
    resultado = datawhatscadchatvwDAO.DataWhatsCadchatVWDAO()
    return resultado.listDataWhatsCadchatVW(request.json)


@app.route("/dictDataWhatsCadchatVW/", methods=["POST"])
def dictDataWhatsCadchatVW():
    resultado = datawhatscadchatvwDAO.DataWhatsCadchatVWDAO()
    return resultado.dictDataWhatsCadchatVW(request.json)


@app.route("/fieldsDataWhatsCadchatVW/", methods=["POST"])
def fieldsDataWhatsCadchatVW():
    resultado = datawhatscadchatvwDAO.DataWhatsCadchatVWDAO()
    return resultado.fieldsDataWhatsCadchatVW(request.json)


@app.route("/findDataWhatsCadchatVW/", methods=["POST"])
def findDataWhatsCadchatVW():
    resultado = datawhatscadchatvwDAO.DataWhatsCadchatVWDAO()
    return resultado.findDataWhatsCadchatVW(request.json)


"""
  Fim rota: DataWhatsCadchatVW
"""

"""
  Rotas do WebService para a classe: Invite
"""
import invite


@app.route("/createInvite/", methods=["POST"])
def createInvite():
    resultado = invite.Invite()
    return resultado.createInvite(request.json)


"""
  Fim rota: Inivte
"""

"""
  Rotas do WebService para a classe: OportunidadeFluxoVW (VW02293)
"""
import oportunidadefluxovwDAO


@app.route("/listOportunidadeFluxoVW/", methods=["POST"])
def listOportunidadeFluxoVW():
    resultado = oportunidadefluxovwDAO.OportunidadeFluxoVWDAO()
    return resultado.listOportunidadeFluxoVW(request.json)


@app.route("/dictOportunidadeFluxoVW/", methods=["POST"])
def dictOportunidadeFluxoVW():
    resultado = oportunidadefluxovwDAO.OportunidadeFluxoVWDAO()
    return resultado.dictOportunidadeFluxoVW(request.json)


@app.route("/fieldsOportunidadeFluxoVW/", methods=["POST"])
def fieldsOportunidadeFluxoVW():
    resultado = oportunidadefluxovwDAO.OportunidadeFluxoVWDAO()
    return resultado.fieldsOportunidadeFluxoVW(request.json)


@app.route("/findOportunidadeFluxoVW/", methods=["POST"])
def findOportunidadeFluxoVW():
    resultado = oportunidadefluxovwDAO.OportunidadeFluxoVWDAO()
    return resultado.findOportunidadeFluxoVW(request.json)


"""
  Fim rota: OportunidadeFluxoVW
"""

"""
  Rotas do WebService para a classe: PrecontratoFluxoVW (VW02294)
"""
import precontratofluxovwDAO


@app.route("/listPrecontratoFluxoVW/", methods=["POST"])
def listPrecontratoFluxoVW():
    resultado = precontratofluxovwDAO.PrecontratoFluxoVWDAO()
    return resultado.listPrecontratoFluxoVW(request.json)


@app.route("/dictPrecontratoFluxoVW/", methods=["POST"])
def dictPrecontratoFluxoVW():
    resultado = precontratofluxovwDAO.PrecontratoFluxoVWDAO()
    return resultado.dictPrecontratoFluxoVW(request.json)


@app.route("/fieldsPrecontratoFluxoVW/", methods=["POST"])
def fieldsPrecontratoFluxoVW():
    resultado = precontratofluxovwDAO.PrecontratoFluxoVWDAO()
    return resultado.fieldsPrecontratoFluxoVW(request.json)


@app.route("/findPrecontratoFluxoVW/", methods=["POST"])
def findPrecontratoFluxoVW():
    resultado = precontratofluxovwDAO.PrecontratoFluxoVWDAO()
    return resultado.findPrecontratoFluxoVW(request.json)


"""
  Fim rota: PrecontratoFluxoVW
"""

"""
  Rotas do WebService para a classe: PermissaoVW (VW00021)
"""
import permissaovwDAO


@app.route("/listPermissaoVW/", methods=["POST"])
def listPermissaoVW():
    resultado = permissaovwDAO.PermissaoVWDAO()
    return resultado.listPermissaoVW(request.json)


@app.route("/dictPermissaoVW/", methods=["POST"])
def dictPermissaoVW():
    resultado = permissaovwDAO.PermissaoVWDAO()
    return resultado.dictPermissaoVW(request.json)


@app.route("/fieldsPermissaoVW/", methods=["POST"])
def fieldsPermissaoVW():
    resultado = permissaovwDAO.PermissaoVWDAO()
    return resultado.fieldsPermissaoVW(request.json)


@app.route("/findPermissaoVW/", methods=["POST"])
def findPermissaoVW():
    resultado = permissaovwDAO.PermissaoVWDAO()
    return resultado.findPermissaoVW(request.json)


"""
  Fim rota: PermissaoVW
"""

"""
  Rotas do WebService para a classe: UsuarioPermissaoVW (VW00020)
"""
import usuariopermissaovwDAO


@app.route("/listUsuarioPermissaoVW/", methods=["POST"])
def listUsuarioPermissaoVW():
    resultado = usuariopermissaovwDAO.UsuarioPermissaoVWDAO()
    return resultado.listUsuarioPermissaoVW(request.json)


@app.route("/dictUsuarioPermissaoVW/", methods=["POST"])
def dictUsuarioPermissaoVW():
    resultado = usuariopermissaovwDAO.UsuarioPermissaoVWDAO()
    return resultado.dictUsuarioPermissaoVW(request.json)


@app.route("/fieldsUsuarioPermissaoVW/", methods=["POST"])
def fieldsUsuarioPermissaoVW():
    resultado = usuariopermissaovwDAO.UsuarioPermissaoVWDAO()
    return resultado.fieldsUsuarioPermissaoVW(request.json)


@app.route("/findUsuarioPermissaoVW/", methods=["POST"])
def findUsuarioPermissaoVW():
    resultado = usuariopermissaovwDAO.UsuarioPermissaoVWDAO()
    return resultado.findUsuarioPermissaoVW(request.json)


"""
  Fim rota: UsuarioPermissaoVW
"""

"""
  Rotas do WebService para a classe: Senha (TB00008)
"""
import senhaDAO


@app.route("/listSenha/", methods=["POST"])
def listSenha():
    resultado = senhaDAO.SenhaDAO()
    return resultado.listSenha(request.json)


@app.route("/dictSenha/", methods=["POST"])
def dictSenha():
    resultado = senhaDAO.SenhaDAO()
    return resultado.dictSenha(request.json)


@app.route("/fieldsSenha/", methods=["POST"])
def fieldsSenha():
    resultado = senhaDAO.SenhaDAO()
    return resultado.fieldsSenha(request.json)


@app.route("/findSenha/", methods=["POST"])
def findSenha():
    resultado = senhaDAO.SenhaDAO()
    return resultado.findSenha(request.json)


@app.route("/SenhaID", methods=["POST"])
def senhaID():
    resultado = senhaDAO.SenhaDAO()
    return resultado.senhaID(request.json)


@app.route("/insSenha", methods=["POST"])
def insSenha():
    resultado = senhaDAO.SenhaDAO()
    return resultado.insSenha(request.json)


@app.route("/updSenha", methods=["POST"])
def updSenha():
    resultado = senhaDAO.SenhaDAO()
    return resultado.updSenha(request.json)


@app.route("/delSenha", methods=["POST"])
def delSenha():
    resultado = senhaDAO.SenhaDAO()
    return resultado.delSenha(request.json)


"""
  Fim rota: Senha
"""

"""
  Rotas do WebService para a classe: ContratoVisaoVW (VW02295)
"""
import contratovisaovwDAO


@app.route("/listContratoVisaoVW/", methods=["POST"])
def listContratoVisaoVW():
    resultado = contratovisaovwDAO.ContratoVisaoVWDAO()
    return resultado.listContratoVisaoVW(request.json)


@app.route("/dictContratoVisaoVW/", methods=["POST"])
def dictContratoVisaoVW():
    resultado = contratovisaovwDAO.ContratoVisaoVWDAO()
    return resultado.dictContratoVisaoVW(request.json)


@app.route("/fieldsContratoVisaoVW/", methods=["POST"])
def fieldsContratoVisaoVW():
    resultado = contratovisaovwDAO.ContratoVisaoVWDAO()
    return resultado.fieldsContratoVisaoVW(request.json)


@app.route("/findContratoVisaoVW/", methods=["POST"])
def findContratoVisaoVW():
    resultado = contratovisaovwDAO.ContratoVisaoVWDAO()
    return resultado.findContratoVisaoVW(request.json)


"""
  Fim rota: ContratoVisaoVW
"""

"""
  Rotas do WebService para a classe: ContratoVisaoEquipamentoVW (VW02297)
"""
import contratovisaoequipamentovwDAO


@app.route("/listContratoVisaoEquipamentoVW/", methods=["POST"])
def listContratoVisaoEquipamentoVW():
    resultado = contratovisaoequipamentovwDAO.ContratoVisaoEquipamentoVWDAO()
    return resultado.listContratoVisaoEquipamentoVW(request.json)


@app.route("/dictContratoVisaoEquipamentoVW/", methods=["POST"])
def dictContratoVisaoEquipamentoVW():
    resultado = contratovisaoequipamentovwDAO.ContratoVisaoEquipamentoVWDAO()
    return resultado.dictContratoVisaoEquipamentoVW(request.json)


@app.route("/fieldsContratoVisaoEquipamentoVW/", methods=["POST"])
def fieldsContratoVisaoEquipamentoVW():
    resultado = contratovisaoequipamentovwDAO.ContratoVisaoEquipamentoVWDAO()
    return resultado.fieldsContratoVisaoEquipamentoVW(request.json)


@app.route("/findContratoVisaoEquipamentoVW/", methods=["POST"])
def findContratoVisaoEquipamentoVW():
    resultado = contratovisaoequipamentovwDAO.ContratoVisaoEquipamentoVWDAO()
    return resultado.findContratoVisaoEquipamentoVW(request.json)


"""
  Fim rota: ContratoVisaoEquipamentoVW
"""

"""
  Rotas do WebService para a classe: OperacaoStatus (TB01092)
"""
import operacaostatusDAO


@app.route("/listOperacaoStatus/", methods=["POST"])
def listOperacaoStatus():
    resultado = operacaostatusDAO.OperacaoStatusDAO()
    return resultado.listOperacaoStatus(request.json)


@app.route("/dictOperacaoStatus/", methods=["POST"])
def dictOperacaoStatus():
    resultado = operacaostatusDAO.OperacaoStatusDAO()
    return resultado.dictOperacaoStatus(request.json)


@app.route("/fieldsOperacaoStatus/", methods=["POST"])
def fieldsOperacaoStatus():
    resultado = operacaostatusDAO.OperacaoStatusDAO()
    return resultado.fieldsOperacaoStatus(request.json)


@app.route("/findOperacaoStatus/", methods=["POST"])
def findOperacaoStatus():
    resultado = operacaostatusDAO.OperacaoStatusDAO()
    return resultado.findOperacaoStatus(request.json)


@app.route("/OperacaoStatusID", methods=["POST"])
def operacaostatusID():
    resultado = operacaostatusDAO.OperacaoStatusDAO()
    return resultado.operacaostatusID(request.json)


@app.route("/insOperacaoStatus", methods=["POST"])
def insOperacaoStatus():
    resultado = operacaostatusDAO.OperacaoStatusDAO()
    return resultado.insOperacaoStatus(request.json)


@app.route("/updOperacaoStatus", methods=["POST"])
def updOperacaoStatus():
    resultado = operacaostatusDAO.OperacaoStatusDAO()
    return resultado.updOperacaoStatus(request.json)


@app.route("/delOperacaoStatus", methods=["POST"])
def delOperacaoStatus():
    resultado = operacaostatusDAO.OperacaoStatusDAO()
    return resultado.delOperacaoStatus(request.json)


"""
  Fim rota: OperacaoStatus
"""

"""
  Rotas do WebService para a classe: OperacaoEmpresa (TB01046)
"""
import operacaoempresaDAO


@app.route("/listOperacaoEmpresa/", methods=["POST"])
def listOperacaoEmpresa():
    resultado = operacaoempresaDAO.OperacaoEmpresaDAO()
    return resultado.listOperacaoEmpresa(request.json)


@app.route("/dictOperacaoEmpresa/", methods=["POST"])
def dictOperacaoEmpresa():
    resultado = operacaoempresaDAO.OperacaoEmpresaDAO()
    return resultado.dictOperacaoEmpresa(request.json)


@app.route("/fieldsOperacaoEmpresa/", methods=["POST"])
def fieldsOperacaoEmpresa():
    resultado = operacaoempresaDAO.OperacaoEmpresaDAO()
    return resultado.fieldsOperacaoEmpresa(request.json)


@app.route("/findOperacaoEmpresa/", methods=["POST"])
def findOperacaoEmpresa():
    resultado = operacaoempresaDAO.OperacaoEmpresaDAO()
    return resultado.findOperacaoEmpresa(request.json)


@app.route("/OperacaoEmpresaID", methods=["POST"])
def operacaoempresaID():
    resultado = operacaoempresaDAO.OperacaoEmpresaDAO()
    return resultado.operacaoempresaID(request.json)


@app.route("/insOperacaoEmpresa", methods=["POST"])
def insOperacaoEmpresa():
    resultado = operacaoempresaDAO.OperacaoEmpresaDAO()
    return resultado.insOperacaoEmpresa(request.json)


@app.route("/updOperacaoEmpresa", methods=["POST"])
def updOperacaoEmpresa():
    resultado = operacaoempresaDAO.OperacaoEmpresaDAO()
    return resultado.updOperacaoEmpresa(request.json)


@app.route("/delOperacaoEmpresa", methods=["POST"])
def delOperacaoEmpresa():
    resultado = operacaoempresaDAO.OperacaoEmpresaDAO()
    return resultado.delOperacaoEmpresa(request.json)


"""
  Fim rota: OperacaoEmpresa
"""

import idtable


@app.route("/getIDTable", methods=["POST"])
def getIDTable():
    resultado = idtable.IDTable()
    return resultado.getIDTable(request.json)


"""
  Fim rota: Dao
"""

"""
  Rotas do WebService para a classe: Historico (TB02130)
"""
import historicoDAO


@app.route("/listHistorico/", methods=["POST"])
def listHistorico():
    resultado = historicoDAO.HistoricoDAO()
    return resultado.listHistorico(request.json)


@app.route("/dictHistorico/", methods=["POST"])
def dictHistorico():
    resultado = historicoDAO.HistoricoDAO()
    return resultado.dictHistorico(request.json)


@app.route("/fieldsHistorico/", methods=["POST"])
def fieldsHistorico():
    resultado = historicoDAO.HistoricoDAO()
    return resultado.fieldsHistorico(request.json)


@app.route("/findHistorico/", methods=["POST"])
def findHistorico():
    resultado = historicoDAO.HistoricoDAO()
    return resultado.findHistorico(request.json)


@app.route("/insHistorico", methods=["POST"])
def insHistorico():
    resultado = historicoDAO.HistoricoDAO()
    return resultado.insHistorico(request.json)


@app.route("/updHistorico", methods=["POST"])
def updHistorico():
    resultado = historicoDAO.HistoricoDAO()
    return resultado.updHistorico(request.json)


@app.route("/delHistorico", methods=["POST"])
def delHistorico():
    resultado = historicoDAO.HistoricoDAO()
    return resultado.delHistorico(request.json)


"""
  Fim rota: Historico
"""

"""
  Rotas do WebService para a classe: Contador (TB00002)
"""
import contadorDAO


@app.route("/listContador/", methods=["POST"])
def listContador():
    resultado = contadorDAO.ContadorDAO()
    return resultado.listContador(request.json)


@app.route("/dictContador/", methods=["POST"])
def dictContador():
    resultado = contadorDAO.ContadorDAO()
    return resultado.dictContador(request.json)


@app.route("/fieldsContador/", methods=["POST"])
def fieldsContador():
    resultado = contadorDAO.ContadorDAO()
    return resultado.fieldsContador(request.json)


@app.route("/findContador/", methods=["POST"])
def findContador():
    resultado = contadorDAO.ContadorDAO()
    return resultado.findContador(request.json)


@app.route("/insContador", methods=["POST"])
def insContador():
    resultado = contadorDAO.ContadorDAO()
    return resultado.insContador(request.json)


@app.route("/updContador", methods=["POST"])
def updContador():
    resultado = contadorDAO.ContadorDAO()
    return resultado.updContador(request.json)


@app.route("/delContador", methods=["POST"])
def delContador():
    resultado = contadorDAO.ContadorDAO()
    return resultado.delContador(request.json)


"""
  Fim rota: Contador
"""

"""
  Rotas do WebService para a classe: GmoReqVW (VW02292)
"""
import gmoreqvwDAO


@app.route("/listGmoReqVW/", methods=["POST"])
def listGmoReqVW():
    resultado = gmoreqvwDAO.GmoReqVWDAO()
    return resultado.listGmoReqVW(request.json)


@app.route("/dictGmoReqVW/", methods=["POST"])
def dictGmoReqVW():
    resultado = gmoreqvwDAO.GmoReqVWDAO()
    return resultado.dictGmoReqVW(request.json)


@app.route("/fieldsGmoReqVW/", methods=["POST"])
def fieldsGmoReqVW():
    resultado = gmoreqvwDAO.GmoReqVWDAO()
    return resultado.fieldsGmoReqVW(request.json)


@app.route("/findGmoReqVW/", methods=["POST"])
def findGmoReqVW():
    resultado = gmoreqvwDAO.GmoReqVWDAO()
    return resultado.findGmoReqVW(request.json)


"""
  Fim rota: GmoReqVW
"""

"""
  Rotas do WebService para a classe: GmoTransitoVW (VW02300)
"""
import gmotransitovwDAO


@app.route("/listGmoTransitoVW/", methods=["POST"])
def listGmoTransitoVW():
    resultado = gmotransitovwDAO.GmoTransitoVWDAO()
    return resultado.listGmoTransitoVW(request.json)


@app.route("/dictGmoTransitoVW/", methods=["POST"])
def dictGmoTransitoVW():
    resultado = gmotransitovwDAO.GmoTransitoVWDAO()
    return resultado.dictGmoTransitoVW(request.json)


@app.route("/fieldsGmoTransitoVW/", methods=["POST"])
def fieldsGmoTransitoVW():
    resultado = gmotransitovwDAO.GmoTransitoVWDAO()
    return resultado.fieldsGmoTransitoVW(request.json)


@app.route("/findGmoTransitoVW/", methods=["POST"])
def findGmoTransitoVW():
    resultado = gmotransitovwDAO.GmoTransitoVWDAO()
    return resultado.findGmoTransitoVW(request.json)


"""
  Fim rota: GmoTransitoVW
"""

"""
  Rotas do WebService para a classe: consultaCNPJ
"""
import cnpj


@app.route('/consultaCNPJ', methods=['GET'])
def minha_rota():
    value = request.args.get('cnpj', '00650512000101')
    retorno = cnpj.consultaCNPJ(value)
    return retorno


"""
  Rotas do WebService para a classe: Compra (TB02002)
"""
import compraDAO


@app.route("/listCompra/", methods=["POST"])
def listCompra():
    resultado = compraDAO.CompraDAO()
    return resultado.listCompra(request.json)


@app.route("/dictCompra/", methods=["POST"])
def dictCompra():
    resultado = compraDAO.CompraDAO()
    return resultado.dictCompra(request.json)


@app.route("/fieldsCompra/", methods=["POST"])
def fieldsCompra():
    resultado = compraDAO.CompraDAO()
    return resultado.fieldsCompra(request.json)


@app.route("/findCompra/", methods=["POST"])
def findCompra():
    resultado = compraDAO.CompraDAO()
    return resultado.findCompra(request.json)


@app.route("/CompraID", methods=["POST"])
def compraID():
    resultado = compraDAO.CompraDAO()
    return resultado.compraID(request.json)


@app.route("/insCompra", methods=["POST"])
def insCompra():
    resultado = compraDAO.CompraDAO()
    return resultado.insCompra(request.json)


@app.route("/updCompra", methods=["POST"])
def updCompra():
    resultado = compraDAO.CompraDAO()
    return resultado.updCompra(request.json)


@app.route("/delCompra", methods=["POST"])
def delCompra():
    resultado = compraDAO.CompraDAO()
    return resultado.delCompra(request.json)


"""
  Fim rota: Compra
"""

"""
  Rotas do WebService para a classe: PedidoCompra (TB02030)
"""
import pedidocompraDAO


@app.route("/listPedidoCompra/", methods=["POST"])
def listPedidoCompra():
    resultado = pedidocompraDAO.PedidoCompraDAO()
    return resultado.listPedidoCompra(request.json)


@app.route("/dictPedidoCompra/", methods=["POST"])
def dictPedidoCompra():
    resultado = pedidocompraDAO.PedidoCompraDAO()
    return resultado.dictPedidoCompra(request.json)


@app.route("/fieldsPedidoCompra/", methods=["POST"])
def fieldsPedidoCompra():
    resultado = pedidocompraDAO.PedidoCompraDAO()
    return resultado.fieldsPedidoCompra(request.json)


@app.route("/findPedidoCompra/", methods=["POST"])
def findPedidoCompra():
    resultado = pedidocompraDAO.PedidoCompraDAO()
    return resultado.findPedidoCompra(request.json)


@app.route("/PedidoCompraID", methods=["POST"])
def pedidocompraID():
    resultado = pedidocompraDAO.PedidoCompraDAO()
    return resultado.pedidocompraID(request.json)


@app.route("/insPedidoCompra", methods=["POST"])
def insPedidoCompra():
    resultado = pedidocompraDAO.PedidoCompraDAO()
    return resultado.insPedidoCompra(request.json)


@app.route("/updPedidoCompra", methods=["POST"])
def updPedidoCompra():
    resultado = pedidocompraDAO.PedidoCompraDAO()
    return resultado.updPedidoCompra(request.json)


@app.route("/delPedidoCompra", methods=["POST"])
def delPedidoCompra():
    resultado = pedidocompraDAO.PedidoCompraDAO()
    return resultado.delPedidoCompra(request.json)


"""
  Fim rota: PedidoCompra
"""

"""
  Rotas do WebService para a classe: OperacaoCompra (TB01078)
"""
import operacaocompraDAO


@app.route("/listOperacaoCompra/", methods=["POST"])
def listOperacaoCompra():
    resultado = operacaocompraDAO.OperacaoCompraDAO()
    return resultado.listOperacaoCompra(request.json)


@app.route("/dictOperacaoCompra/", methods=["POST"])
def dictOperacaoCompra():
    resultado = operacaocompraDAO.OperacaoCompraDAO()
    return resultado.dictOperacaoCompra(request.json)


@app.route("/fieldsOperacaoCompra/", methods=["POST"])
def fieldsOperacaoCompra():
    resultado = operacaocompraDAO.OperacaoCompraDAO()
    return resultado.fieldsOperacaoCompra(request.json)


@app.route("/findOperacaoCompra/", methods=["POST"])
def findOperacaoCompra():
    resultado = operacaocompraDAO.OperacaoCompraDAO()
    return resultado.findOperacaoCompra(request.json)


@app.route("/OperacaoCompraID", methods=["POST"])
def operacaocompraID():
    resultado = operacaocompraDAO.OperacaoCompraDAO()
    return resultado.operacaocompraID(request.json)


@app.route("/insOperacaoCompra", methods=["POST"])
def insOperacaoCompra():
    resultado = operacaocompraDAO.OperacaoCompraDAO()
    return resultado.insOperacaoCompra(request.json)


@app.route("/updOperacaoCompra", methods=["POST"])
def updOperacaoCompra():
    resultado = operacaocompraDAO.OperacaoCompraDAO()
    return resultado.updOperacaoCompra(request.json)


@app.route("/delOperacaoCompra", methods=["POST"])
def delOperacaoCompra():
    resultado = operacaocompraDAO.OperacaoCompraDAO()
    return resultado.delOperacaoCompra(request.json)


"""
  Fim rota: OperacaoCompra
"""

"""
  Rotas do WebService para a classe: Transportadora (TB01009)
"""
import transportadoraDAO


@app.route("/listTransportadora/", methods=["POST"])
def listTransportadora():
    resultado = transportadoraDAO.TransportadoraDAO()
    return resultado.listTransportadora(request.json)


@app.route("/dictTransportadora/", methods=["POST"])
def dictTransportadora():
    resultado = transportadoraDAO.TransportadoraDAO()
    return resultado.dictTransportadora(request.json)


@app.route("/fieldsTransportadora/", methods=["POST"])
def fieldsTransportadora():
    resultado = transportadoraDAO.TransportadoraDAO()
    return resultado.fieldsTransportadora(request.json)


@app.route("/findTransportadora/", methods=["POST"])
def findTransportadora():
    resultado = transportadoraDAO.TransportadoraDAO()
    return resultado.findTransportadora(request.json)


@app.route("/TransportadoraID", methods=["POST"])
def transportadoraID():
    resultado = transportadoraDAO.TransportadoraDAO()
    return resultado.transportadoraID(request.json)


@app.route("/insTransportadora", methods=["POST"])
def insTransportadora():
    resultado = transportadoraDAO.TransportadoraDAO()
    return resultado.insTransportadora(request.json)


@app.route("/updTransportadora", methods=["POST"])
def updTransportadora():
    resultado = transportadoraDAO.TransportadoraDAO()
    return resultado.updTransportadora(request.json)


@app.route("/delTransportadora", methods=["POST"])
def delTransportadora():
    resultado = transportadoraDAO.TransportadoraDAO()
    return resultado.delTransportadora(request.json)


"""
  Fim rota: Transportadora
"""

"""
  Rotas do WebService para a classe: Statuscom (TB01039)
"""
import statuscomDAO


@app.route("/listStatuscom/", methods=["POST"])
def listStatuscom():
    resultado = statuscomDAO.StatuscomDAO()
    return resultado.listStatuscom(request.json)


@app.route("/dictStatuscom/", methods=["POST"])
def dictStatuscom():
    resultado = statuscomDAO.StatuscomDAO()
    return resultado.dictStatuscom(request.json)


@app.route("/fieldsStatuscom/", methods=["POST"])
def fieldsStatuscom():
    resultado = statuscomDAO.StatuscomDAO()
    return resultado.fieldsStatuscom(request.json)


@app.route("/findStatuscom/", methods=["POST"])
def findStatuscom():
    resultado = statuscomDAO.StatuscomDAO()
    return resultado.findStatuscom(request.json)


@app.route("/StatuscomID", methods=["POST"])
def statuscomID():
    resultado = statuscomDAO.StatuscomDAO()
    return resultado.statuscomID(request.json)


@app.route("/insStatuscom", methods=["POST"])
def insStatuscom():
    resultado = statuscomDAO.StatuscomDAO()
    return resultado.insStatuscom(request.json)


@app.route("/updStatuscom", methods=["POST"])
def updStatuscom():
    resultado = statuscomDAO.StatuscomDAO()
    return resultado.updStatuscom(request.json)


@app.route("/delStatuscom", methods=["POST"])
def delStatuscom():
    resultado = statuscomDAO.StatuscomDAO()
    return resultado.delStatuscom(request.json)


"""
  Fim rota: Statuscom
"""

"""
  Rotas do WebService para a classe: GmoComVW (VW02301)
"""
import gmocomvwDAO


@app.route("/listGmoComVW/", methods=["POST"])
def listGmoComVW():
    resultado = gmocomvwDAO.GmoComVWDAO()
    return resultado.listGmoComVW(request.json)


@app.route("/dictGmoComVW/", methods=["POST"])
def dictGmoComVW():
    resultado = gmocomvwDAO.GmoComVWDAO()
    return resultado.dictGmoComVW(request.json)


@app.route("/fieldsGmoComVW/", methods=["POST"])
def fieldsGmoComVW():
    resultado = gmocomvwDAO.GmoComVWDAO()
    return resultado.fieldsGmoComVW(request.json)


@app.route("/findGmoComVW/", methods=["POST"])
def findGmoComVW():
    resultado = gmocomvwDAO.GmoComVWDAO()
    return resultado.findGmoComVW(request.json)


"""
  Fim rota: GmoComVW
"""

"""
  Rotas do WebService para a classe: DatawhatsNotificacao (TB08003)
"""
import datawhatsnotificacaoDAO


@app.route("/listDatawhatsNotificacao/", methods=["POST"])
def listDatawhatsNotificacao():
    resultado = datawhatsnotificacaoDAO.DatawhatsNotificacaoDAO()
    return resultado.listDatawhatsNotificacao(request.json)


@app.route("/dictDatawhatsNotificacao/", methods=["POST"])
def dictDatawhatsNotificacao():
    resultado = datawhatsnotificacaoDAO.DatawhatsNotificacaoDAO()
    return resultado.dictDatawhatsNotificacao(request.json)


@app.route("/fieldsDatawhatsNotificacao/", methods=["POST"])
def fieldsDatawhatsNotificacao():
    resultado = datawhatsnotificacaoDAO.DatawhatsNotificacaoDAO()
    return resultado.fieldsDatawhatsNotificacao(request.json)


@app.route("/findDatawhatsNotificacao/", methods=["POST"])
def findDatawhatsNotificacao():
    resultado = datawhatsnotificacaoDAO.DatawhatsNotificacaoDAO()
    return resultado.findDatawhatsNotificacao(request.json)


@app.route("/insDatawhatsNotificacao", methods=["POST"])
def insDatawhatsNotificacao():
    resultado = datawhatsnotificacaoDAO.DatawhatsNotificacaoDAO()
    return resultado.insDatawhatsNotificacao(request.json)


@app.route("/updDatawhatsNotificacao", methods=["POST"])
def updDatawhatsNotificacao():
    resultado = datawhatsnotificacaoDAO.DatawhatsNotificacaoDAO()
    return resultado.updDatawhatsNotificacao(request.json)


@app.route("/delDatawhatsNotificacao", methods=["POST"])
def delDatawhatsNotificacao():
    resultado = datawhatsnotificacaoDAO.DatawhatsNotificacaoDAO()
    return resultado.delDatawhatsNotificacao(request.json)


"""
  Fim rota: DatawhatsNotificacao
"""

"""
  Rotas do WebService para a classe: Query (TB00113)
"""
import queryDAO


@app.route("/listQuery/", methods=["POST"])
def listQuery():
    resultado = queryDAO.QueryDAO()
    return resultado.listQuery(request.json)


@app.route("/dictQuery/", methods=["POST"])
def dictQuery():
    resultado = queryDAO.QueryDAO()
    return resultado.dictQuery(request.json)


@app.route("/fieldsQuery/", methods=["POST"])
def fieldsQuery():
    resultado = queryDAO.QueryDAO()
    return resultado.fieldsQuery(request.json)


@app.route("/findQuery/", methods=["POST"])
def findQuery():
    resultado = queryDAO.QueryDAO()
    return resultado.findQuery(request.json)


@app.route("/QueryID", methods=["POST"])
def queryID():
    resultado = queryDAO.QueryDAO()
    return resultado.queryID(request.json)


@app.route("/insQuery", methods=["POST"])
def insQuery():
    resultado = queryDAO.QueryDAO()
    return resultado.insQuery(request.json)


@app.route("/updQuery", methods=["POST"])
def updQuery():
    resultado = queryDAO.QueryDAO()
    return resultado.updQuery(request.json)


@app.route("/delQuery", methods=["POST"])
def delQuery():
    resultado = queryDAO.QueryDAO()
    return resultado.delQuery(request.json)


"""
  Fim rota: Query
"""

"""
  Rotas do WebService para a classe: QueryParam (TB00114)
"""
import queryparamDAO


@app.route("/listQueryParam/", methods=["POST"])
def listQueryParam():
    resultado = queryparamDAO.QueryParamDAO()
    return resultado.listQueryParam(request.json)


@app.route("/dictQueryParam/", methods=["POST"])
def dictQueryParam():
    resultado = queryparamDAO.QueryParamDAO()
    return resultado.dictQueryParam(request.json)


@app.route("/fieldsQueryParam/", methods=["POST"])
def fieldsQueryParam():
    resultado = queryparamDAO.QueryParamDAO()
    return resultado.fieldsQueryParam(request.json)


@app.route("/findQueryParam/", methods=["POST"])
def findQueryParam():
    resultado = queryparamDAO.QueryParamDAO()
    return resultado.findQueryParam(request.json)


@app.route("/insQueryParam", methods=["POST"])
def insQueryParam():
    resultado = queryparamDAO.QueryParamDAO()
    return resultado.insQueryParam(request.json)


@app.route("/updQueryParam", methods=["POST"])
def updQueryParam():
    resultado = queryparamDAO.QueryParamDAO()
    return resultado.updQueryParam(request.json)


@app.route("/delQueryParam", methods=["POST"])
def delQueryParam():
    resultado = queryparamDAO.QueryParamDAO()
    return resultado.delQueryParam(request.json)


"""
  Fim rota: QueryParam
"""

"""
  Rotas do WebService para a classe: Dashboard (TB00115)
"""
import dashboardDAO


@app.route("/listDashboard/", methods=["POST"])
def listDashboard():
    resultado = dashboardDAO.DashboardDAO()
    return resultado.listDashboard(request.json)


@app.route("/dictDashboard/", methods=["POST"])
def dictDashboard():
    resultado = dashboardDAO.DashboardDAO()
    return resultado.dictDashboard(request.json)


@app.route("/fieldsDashboard/", methods=["POST"])
def fieldsDashboard():
    resultado = dashboardDAO.DashboardDAO()
    return resultado.fieldsDashboard(request.json)


@app.route("/findDashboard/", methods=["POST"])
def findDashboard():
    resultado = dashboardDAO.DashboardDAO()
    return resultado.findDashboard(request.json)


@app.route("/DashboardID", methods=["POST"])
def dashboardID():
    resultado = dashboardDAO.DashboardDAO()
    return resultado.dashboardID(request.json)


@app.route("/insDashboard", methods=["POST"])
def insDashboard():
    resultado = dashboardDAO.DashboardDAO()
    return resultado.insDashboard(request.json)


@app.route("/updDashboard", methods=["POST"])
def updDashboard():
    resultado = dashboardDAO.DashboardDAO()
    return resultado.updDashboard(request.json)


@app.route("/delDashboard", methods=["POST"])
def delDashboard():
    resultado = dashboardDAO.DashboardDAO()
    return resultado.delDashboard(request.json)


"""
  Fim rota: Dashboard
"""

"""
  Rotas do WebService para a classe: DashboardQuery (TB00116)
"""
import dashboardqueryDAO


@app.route("/listDashboardQuery/", methods=["POST"])
def listDashboardQuery():
    resultado = dashboardqueryDAO.DashboardQueryDAO()
    return resultado.listDashboardQuery(request.json)


@app.route("/dictDashboardQuery/", methods=["POST"])
def dictDashboardQuery():
    resultado = dashboardqueryDAO.DashboardQueryDAO()
    return resultado.dictDashboardQuery(request.json)


@app.route("/fieldsDashboardQuery/", methods=["POST"])
def fieldsDashboardQuery():
    resultado = dashboardqueryDAO.DashboardQueryDAO()
    return resultado.fieldsDashboardQuery(request.json)


@app.route("/findDashboardQuery/", methods=["POST"])
def findDashboardQuery():
    resultado = dashboardqueryDAO.DashboardQueryDAO()
    return resultado.findDashboardQuery(request.json)


@app.route("/insDashboardQuery", methods=["POST"])
def insDashboardQuery():
    resultado = dashboardqueryDAO.DashboardQueryDAO()
    return resultado.insDashboardQuery(request.json)


@app.route("/updDashboardQuery", methods=["POST"])
def updDashboardQuery():
    resultado = dashboardqueryDAO.DashboardQueryDAO()
    return resultado.updDashboardQuery(request.json)


@app.route("/delDashboardQuery", methods=["POST"])
def delDashboardQuery():
    resultado = dashboardqueryDAO.DashboardQueryDAO()
    return resultado.delDashboardQuery(request.json)


"""
  Fim rota: DashboardQuery
"""

"""
  Rotas do WebService para a classe: DashboardUser (TB00117)
"""
import dashboarduserDAO


@app.route("/listDashboardUser/", methods=["POST"])
def listDashboardUser():
    resultado = dashboarduserDAO.DashboardUserDAO()
    return resultado.listDashboardUser(request.json)


@app.route("/dictDashboardUser/", methods=["POST"])
def dictDashboardUser():
    resultado = dashboarduserDAO.DashboardUserDAO()
    return resultado.dictDashboardUser(request.json)


@app.route("/fieldsDashboardUser/", methods=["POST"])
def fieldsDashboardUser():
    resultado = dashboarduserDAO.DashboardUserDAO()
    return resultado.fieldsDashboardUser(request.json)


@app.route("/findDashboardUser/", methods=["POST"])
def findDashboardUser():
    resultado = dashboarduserDAO.DashboardUserDAO()
    return resultado.findDashboardUser(request.json)


@app.route("/insDashboardUser", methods=["POST"])
def insDashboardUser():
    resultado = dashboarduserDAO.DashboardUserDAO()
    return resultado.insDashboardUser(request.json)


@app.route("/updDashboardUser", methods=["POST"])
def updDashboardUser():
    resultado = dashboarduserDAO.DashboardUserDAO()
    return resultado.updDashboardUser(request.json)


@app.route("/delDashboardUser", methods=["POST"])
def delDashboardUser():
    resultado = dashboarduserDAO.DashboardUserDAO()
    return resultado.delDashboardUser(request.json)


"""
  Fim rota: DashboardUser
"""

"""
  Rotas do WebService para a classe: DashboardModule (TB00118)
"""
import dashboardmoduleDAO


@app.route("/listDashboardModule/", methods=["POST"])
def listDashboardModule():
    resultado = dashboardmoduleDAO.DashboardModuleDAO()
    return resultado.listDashboardModule(request.json)


@app.route("/dictDashboardModule/", methods=["POST"])
def dictDashboardModule():
    resultado = dashboardmoduleDAO.DashboardModuleDAO()
    return resultado.dictDashboardModule(request.json)


@app.route("/fieldsDashboardModule/", methods=["POST"])
def fieldsDashboardModule():
    resultado = dashboardmoduleDAO.DashboardModuleDAO()
    return resultado.fieldsDashboardModule(request.json)


@app.route("/findDashboardModule/", methods=["POST"])
def findDashboardModule():
    resultado = dashboardmoduleDAO.DashboardModuleDAO()
    return resultado.findDashboardModule(request.json)


@app.route("/insDashboardModule", methods=["POST"])
def insDashboardModule():
    resultado = dashboardmoduleDAO.DashboardModuleDAO()
    return resultado.insDashboardModule(request.json)


@app.route("/updDashboardModule", methods=["POST"])
def updDashboardModule():
    resultado = dashboardmoduleDAO.DashboardModuleDAO()
    return resultado.updDashboardModule(request.json)


@app.route("/delDashboardModule", methods=["POST"])
def delDashboardModule():
    resultado = dashboardmoduleDAO.DashboardModuleDAO()
    return resultado.delDashboardModule(request.json)


"""
  Fim rota: DashboardModule
"""

"""
  Rotas do WebService para a classe: DashboardSystem (TB00119)
"""
import dashboardsystemDAO


@app.route("/listDashboardSystem/", methods=["POST"])
def listDashboardSystem():
    resultado = dashboardsystemDAO.DashboardSystemDAO()
    return resultado.listDashboardSystem(request.json)


@app.route("/dictDashboardSystem/", methods=["POST"])
def dictDashboardSystem():
    resultado = dashboardsystemDAO.DashboardSystemDAO()
    return resultado.dictDashboardSystem(request.json)


@app.route("/fieldsDashboardSystem/", methods=["POST"])
def fieldsDashboardSystem():
    resultado = dashboardsystemDAO.DashboardSystemDAO()
    return resultado.fieldsDashboardSystem(request.json)


@app.route("/findDashboardSystem/", methods=["POST"])
def findDashboardSystem():
    resultado = dashboardsystemDAO.DashboardSystemDAO()
    return resultado.findDashboardSystem(request.json)


@app.route("/insDashboardSystem", methods=["POST"])
def insDashboardSystem():
    resultado = dashboardsystemDAO.DashboardSystemDAO()
    return resultado.insDashboardSystem(request.json)


@app.route("/updDashboardSystem", methods=["POST"])
def updDashboardSystem():
    resultado = dashboardsystemDAO.DashboardSystemDAO()
    return resultado.updDashboardSystem(request.json)


@app.route("/delDashboardSystem", methods=["POST"])
def delDashboardSystem():
    resultado = dashboardsystemDAO.DashboardSystemDAO()
    return resultado.delDashboardSystem(request.json)


"""
  Fim rota: DashboardSystem
"""

"""
  Rotas do WebService para a classe: DashboardQueryVW (VW00022)
"""
import dashboardqueryvwDAO


@app.route("/listDashboardQueryVW/", methods=["POST"])
def listDashboardQueryVW():
    resultado = dashboardqueryvwDAO.DashboardQueryVWDAO()
    return resultado.listDashboardQueryVW(request.json)


@app.route("/dictDashboardQueryVW/", methods=["POST"])
def dictDashboardQueryVW():
    resultado = dashboardqueryvwDAO.DashboardQueryVWDAO()
    return resultado.dictDashboardQueryVW(request.json)


@app.route("/fieldsDashboardQueryVW/", methods=["POST"])
def fieldsDashboardQueryVW():
    resultado = dashboardqueryvwDAO.DashboardQueryVWDAO()
    return resultado.fieldsDashboardQueryVW(request.json)


@app.route("/findDashboardQueryVW/", methods=["POST"])
def findDashboardQueryVW():
    resultado = dashboardqueryvwDAO.DashboardQueryVWDAO()
    return resultado.findDashboardQueryVW(request.json)


"""
  Fim rota: DashboardQueryVW
"""

"""
  Rotas do WebService para a classe: DashboardUserVW (VW00023)
"""
import dashboarduservwDAO


@app.route("/listDashboardUserVW/", methods=["POST"])
def listDashboardUserVW():
    resultado = dashboarduservwDAO.DashboardUserVWDAO()
    return resultado.listDashboardUserVW(request.json)


@app.route("/dictDashboardUserVW/", methods=["POST"])
def dictDashboardUserVW():
    resultado = dashboarduservwDAO.DashboardUserVWDAO()
    return resultado.dictDashboardUserVW(request.json)


@app.route("/fieldsDashboardUserVW/", methods=["POST"])
def fieldsDashboardUserVW():
    resultado = dashboarduservwDAO.DashboardUserVWDAO()
    return resultado.fieldsDashboardUserVW(request.json)


@app.route("/findDashboardUserVW/", methods=["POST"])
def findDashboardUserVW():
    resultado = dashboarduservwDAO.DashboardUserVWDAO()
    return resultado.findDashboardUserVW(request.json)


"""
  Fim rota: DashboardUserVW
"""

"""
  Rotas do WebService para a classe: DashboardParamVW (VW00024)
"""
import dashboardparamvwDAO


@app.route("/listDashboardParamVW/", methods=["POST"])
def listDashboardParamVW():
    resultado = dashboardparamvwDAO.DashboardParamVWDAO()
    return resultado.listDashboardParamVW(request.json)


@app.route("/dictDashboardParamVW/", methods=["POST"])
def dictDashboardParamVW():
    resultado = dashboardparamvwDAO.DashboardParamVWDAO()
    return resultado.dictDashboardParamVW(request.json)


@app.route("/fieldsDashboardParamVW/", methods=["POST"])
def fieldsDashboardParamVW():
    resultado = dashboardparamvwDAO.DashboardParamVWDAO()
    return resultado.fieldsDashboardParamVW(request.json)


@app.route("/findDashboardParamVW/", methods=["POST"])
def findDashboardParamVW():
    resultado = dashboardparamvwDAO.DashboardParamVWDAO()
    return resultado.findDashboardParamVW(request.json)


"""
  Fim rota: DashboardParamVW
"""

"""
  Rotas do WebService para a classe: Modulo (TB00120)
"""
import moduloDAO


@app.route("/listModulo/", methods=["POST"])
def listModulo():
    resultado = moduloDAO.ModuloDAO()
    return resultado.listModulo(request.json)


@app.route("/dictModulo/", methods=["POST"])
def dictModulo():
    resultado = moduloDAO.ModuloDAO()
    return resultado.dictModulo(request.json)


@app.route("/fieldsModulo/", methods=["POST"])
def fieldsModulo():
    resultado = moduloDAO.ModuloDAO()
    return resultado.fieldsModulo(request.json)


@app.route("/findModulo/", methods=["POST"])
def findModulo():
    resultado = moduloDAO.ModuloDAO()
    return resultado.findModulo(request.json)


@app.route("/insModulo", methods=["POST"])
def insModulo():
    resultado = moduloDAO.ModuloDAO()
    return resultado.insModulo(request.json)


@app.route("/updModulo", methods=["POST"])
def updModulo():
    resultado = moduloDAO.ModuloDAO()
    return resultado.updModulo(request.json)


@app.route("/delModulo", methods=["POST"])
def delModulo():
    resultado = moduloDAO.ModuloDAO()
    return resultado.delModulo(request.json)


"""
  Fim rota: Modulo
"""

"""
  Rotas do WebService para a classe: ClienteProduto (TB01142)
"""
import clienteprodutoDAO


@app.route("/listClienteProduto/", methods=["POST"])
def listClienteProduto():
    resultado = clienteprodutoDAO.ClienteProdutoDAO()
    return resultado.listClienteProduto(request.json)


@app.route("/dictClienteProduto/", methods=["POST"])
def dictClienteProduto():
    resultado = clienteprodutoDAO.ClienteProdutoDAO()
    return resultado.dictClienteProduto(request.json)


@app.route("/fieldsClienteProduto/", methods=["POST"])
def fieldsClienteProduto():
    resultado = clienteprodutoDAO.ClienteProdutoDAO()
    return resultado.fieldsClienteProduto(request.json)


@app.route("/findClienteProduto/", methods=["POST"])
def findClienteProduto():
    resultado = clienteprodutoDAO.ClienteProdutoDAO()
    return resultado.findClienteProduto(request.json)


@app.route("/insClienteProduto", methods=["POST"])
def insClienteProduto():
    resultado = clienteprodutoDAO.ClienteProdutoDAO()
    return resultado.insClienteProduto(request.json)


@app.route("/updClienteProduto", methods=["POST"])
def updClienteProduto():
    resultado = clienteprodutoDAO.ClienteProdutoDAO()
    return resultado.updClienteProduto(request.json)


@app.route("/delClienteProduto", methods=["POST"])
def delClienteProduto():
    resultado = clienteprodutoDAO.ClienteProdutoDAO()
    return resultado.delClienteProduto(request.json)


"""
  Fim rota: ClienteProduto
"""

"""
  Rotas do WebService para a classe: ContratoSiteVW (VW02233)
"""
import contratositevwDAO


@app.route("/listContratoSiteVW/", methods=["POST"])
def listContratoSiteVW():
    resultado = contratositevwDAO.ContratoSiteVWDAO()
    return resultado.listContratoSiteVW(request.json)


@app.route("/dictContratoSiteVW/", methods=["POST"])
def dictContratoSiteVW():
    resultado = contratositevwDAO.ContratoSiteVWDAO()
    return resultado.dictContratoSiteVW(request.json)


@app.route("/fieldsContratoSiteVW/", methods=["POST"])
def fieldsContratoSiteVW():
    resultado = contratositevwDAO.ContratoSiteVWDAO()
    return resultado.fieldsContratoSiteVW(request.json)


@app.route("/findContratoSiteVW/", methods=["POST"])
def findContratoSiteVW():
    resultado = contratositevwDAO.ContratoSiteVWDAO()
    return resultado.findContratoSiteVW(request.json)


"""
  Fim rota: ContratoSiteVW
"""

"""
  Rotas do WebService para a classe: ClienteProdutoVW (VW01133)
"""
import clienteprodutovwDAO


@app.route("/listClienteProdutoVW/", methods=["POST"])
def listClienteProdutoVW():
    resultado = clienteprodutovwDAO.ClienteProdutoVWDAO()
    return resultado.listClienteProdutoVW(request.json)


@app.route("/dictClienteProdutoVW/", methods=["POST"])
def dictClienteProdutoVW():
    resultado = clienteprodutovwDAO.ClienteProdutoVWDAO()
    return resultado.dictClienteProdutoVW(request.json)


@app.route("/fieldsClienteProdutoVW/", methods=["POST"])
def fieldsClienteProdutoVW():
    resultado = clienteprodutovwDAO.ClienteProdutoVWDAO()
    return resultado.fieldsClienteProdutoVW(request.json)


@app.route("/findClienteProdutoVW/", methods=["POST"])
def findClienteProdutoVW():
    resultado = clienteprodutovwDAO.ClienteProdutoVWDAO()
    return resultado.findClienteProdutoVW(request.json)


"""
  Fim rota: ClienteProdutoVW
"""

"""
  Rotas do WebService para a classe: ClienteEstado (TB01147)
"""
import clienteestadoDAO


@app.route("/listClienteEstado/", methods=["POST"])
def listClienteEstado():
    resultado = clienteestadoDAO.ClienteEstadoDAO()
    return resultado.listClienteEstado(request.json)


@app.route("/dictClienteEstado/", methods=["POST"])
def dictClienteEstado():
    resultado = clienteestadoDAO.ClienteEstadoDAO()
    return resultado.dictClienteEstado(request.json)


@app.route("/fieldsClienteEstado/", methods=["POST"])
def fieldsClienteEstado():
    resultado = clienteestadoDAO.ClienteEstadoDAO()
    return resultado.fieldsClienteEstado(request.json)


@app.route("/findClienteEstado/", methods=["POST"])
def findClienteEstado():
    resultado = clienteestadoDAO.ClienteEstadoDAO()
    return resultado.findClienteEstado(request.json)


@app.route("/insClienteEstado", methods=["POST"])
def insClienteEstado():
    resultado = clienteestadoDAO.ClienteEstadoDAO()
    return resultado.insClienteEstado(request.json)


@app.route("/updClienteEstado", methods=["POST"])
def updClienteEstado():
    resultado = clienteestadoDAO.ClienteEstadoDAO()
    return resultado.updClienteEstado(request.json)


@app.route("/delClienteEstado", methods=["POST"])
def delClienteEstado():
    resultado = clienteestadoDAO.ClienteEstadoDAO()
    return resultado.delClienteEstado(request.json)


"""
  Fim rota: ClienteEstado
"""

"""
  Rotas do WebService para a classe: PartnerStatus (TB01148)
"""
import partnerstatusDAO


@app.route("/listPartnerStatus/", methods=["POST"])
def listPartnerStatus():
    resultado = partnerstatusDAO.PartnerStatusDAO()
    return resultado.listPartnerStatus(request.json)


@app.route("/dictPartnerStatus/", methods=["POST"])
def dictPartnerStatus():
    resultado = partnerstatusDAO.PartnerStatusDAO()
    return resultado.dictPartnerStatus(request.json)


@app.route("/fieldsPartnerStatus/", methods=["POST"])
def fieldsPartnerStatus():
    resultado = partnerstatusDAO.PartnerStatusDAO()
    return resultado.fieldsPartnerStatus(request.json)


@app.route("/findPartnerStatus/", methods=["POST"])
def findPartnerStatus():
    resultado = partnerstatusDAO.PartnerStatusDAO()
    return resultado.findPartnerStatus(request.json)


@app.route("/PartnerStatusID", methods=["POST"])
def partnerstatusID():
    resultado = partnerstatusDAO.PartnerStatusDAO()
    return resultado.partnerstatusID(request.json)


@app.route("/insPartnerStatus", methods=["POST"])
def insPartnerStatus():
    resultado = partnerstatusDAO.PartnerStatusDAO()
    return resultado.insPartnerStatus(request.json)


@app.route("/updPartnerStatus", methods=["POST"])
def updPartnerStatus():
    resultado = partnerstatusDAO.PartnerStatusDAO()
    return resultado.updPartnerStatus(request.json)


@app.route("/delPartnerStatus", methods=["POST"])
def delPartnerStatus():
    resultado = partnerstatusDAO.PartnerStatusDAO()
    return resultado.delPartnerStatus(request.json)


"""
  Fim rota: PartnerStatus
"""

"""
  Rotas do WebService para a classe: PartnerWorkflow (TB01149)
"""
import partnerworkflowDAO


@app.route("/listPartnerWorkflow/", methods=["POST"])
def listPartnerWorkflow():
    resultado = partnerworkflowDAO.PartnerWorkflowDAO()
    return resultado.listPartnerWorkflow(request.json)


@app.route("/dictPartnerWorkflow/", methods=["POST"])
def dictPartnerWorkflow():
    resultado = partnerworkflowDAO.PartnerWorkflowDAO()
    return resultado.dictPartnerWorkflow(request.json)


@app.route("/fieldsPartnerWorkflow/", methods=["POST"])
def fieldsPartnerWorkflow():
    resultado = partnerworkflowDAO.PartnerWorkflowDAO()
    return resultado.fieldsPartnerWorkflow(request.json)


@app.route("/findPartnerWorkflow/", methods=["POST"])
def findPartnerWorkflow():
    resultado = partnerworkflowDAO.PartnerWorkflowDAO()
    return resultado.findPartnerWorkflow(request.json)


@app.route("/insPartnerWorkflow", methods=["POST"])
def insPartnerWorkflow():
    resultado = partnerworkflowDAO.PartnerWorkflowDAO()
    return resultado.insPartnerWorkflow(request.json)


@app.route("/updPartnerWorkflow", methods=["POST"])
def updPartnerWorkflow():
    resultado = partnerworkflowDAO.PartnerWorkflowDAO()
    return resultado.updPartnerWorkflow(request.json)


@app.route("/delPartnerWorkflow", methods=["POST"])
def delPartnerWorkflow():
    resultado = partnerworkflowDAO.PartnerWorkflowDAO()
    return resultado.delPartnerWorkflow(request.json)


"""
  Fim rota: PartnerWorkflow
"""

"""
  Rotas do WebService para a classe: PartnerUser (TB01150)
"""
import partneruserDAO


@app.route("/listPartnerUser/", methods=["POST"])
def listPartnerUser():
    resultado = partneruserDAO.PartnerUserDAO()
    return resultado.listPartnerUser(request.json)


@app.route("/dictPartnerUser/", methods=["POST"])
def dictPartnerUser():
    resultado = partneruserDAO.PartnerUserDAO()
    return resultado.dictPartnerUser(request.json)


@app.route("/fieldsPartnerUser/", methods=["POST"])
def fieldsPartnerUser():
    resultado = partneruserDAO.PartnerUserDAO()
    return resultado.fieldsPartnerUser(request.json)


@app.route("/findPartnerUser/", methods=["POST"])
def findPartnerUser():
    resultado = partneruserDAO.PartnerUserDAO()
    return resultado.findPartnerUser(request.json)


@app.route("/insPartnerUser", methods=["POST"])
def insPartnerUser():
    resultado = partneruserDAO.PartnerUserDAO()
    return resultado.insPartnerUser(request.json)


@app.route("/updPartnerUser", methods=["POST"])
def updPartnerUser():
    resultado = partneruserDAO.PartnerUserDAO()
    return resultado.updPartnerUser(request.json)


@app.route("/delPartnerUser", methods=["POST"])
def delPartnerUser():
    resultado = partneruserDAO.PartnerUserDAO()
    return resultado.delPartnerUser(request.json)


"""
  Fim rota: PartnerUser
"""

"""
  Rotas do WebService para a classe: PartnerNotiication (TB01151)
"""
import partnernotiicationDAO


@app.route("/listPartnerNotiication/", methods=["POST"])
def listPartnerNotiication():
    resultado = partnernotiicationDAO.PartnerNotiicationDAO()
    return resultado.listPartnerNotiication(request.json)


@app.route("/dictPartnerNotiication/", methods=["POST"])
def dictPartnerNotiication():
    resultado = partnernotiicationDAO.PartnerNotiicationDAO()
    return resultado.dictPartnerNotiication(request.json)


@app.route("/fieldsPartnerNotiication/", methods=["POST"])
def fieldsPartnerNotiication():
    resultado = partnernotiicationDAO.PartnerNotiicationDAO()
    return resultado.fieldsPartnerNotiication(request.json)


@app.route("/findPartnerNotiication/", methods=["POST"])
def findPartnerNotiication():
    resultado = partnernotiicationDAO.PartnerNotiicationDAO()
    return resultado.findPartnerNotiication(request.json)


@app.route("/insPartnerNotiication", methods=["POST"])
def insPartnerNotiication():
    resultado = partnernotiicationDAO.PartnerNotiicationDAO()
    return resultado.insPartnerNotiication(request.json)


@app.route("/updPartnerNotiication", methods=["POST"])
def updPartnerNotiication():
    resultado = partnernotiicationDAO.PartnerNotiicationDAO()
    return resultado.updPartnerNotiication(request.json)


@app.route("/delPartnerNotiication", methods=["POST"])
def delPartnerNotiication():
    resultado = partnernotiicationDAO.PartnerNotiicationDAO()
    return resultado.delPartnerNotiication(request.json)


"""
  Fim rota: PartnerNotiication
"""

"""
  Rotas do WebService para a classe: PartnerTipo (TB01152)
"""
import partnertipoDAO


@app.route("/listPartnerTipo/", methods=["POST"])
def listPartnerTipo():
    resultado = partnertipoDAO.PartnerTipoDAO()
    return resultado.listPartnerTipo(request.json)


@app.route("/dictPartnerTipo/", methods=["POST"])
def dictPartnerTipo():
    resultado = partnertipoDAO.PartnerTipoDAO()
    return resultado.dictPartnerTipo(request.json)


@app.route("/fieldsPartnerTipo/", methods=["POST"])
def fieldsPartnerTipo():
    resultado = partnertipoDAO.PartnerTipoDAO()
    return resultado.fieldsPartnerTipo(request.json)


@app.route("/findPartnerTipo/", methods=["POST"])
def findPartnerTipo():
    resultado = partnertipoDAO.PartnerTipoDAO()
    return resultado.findPartnerTipo(request.json)


@app.route("/PartnerTipoID", methods=["POST"])
def partnertipoID():
    resultado = partnertipoDAO.PartnerTipoDAO()
    return resultado.partnertipoID(request.json)


@app.route("/insPartnerTipo", methods=["POST"])
def insPartnerTipo():
    resultado = partnertipoDAO.PartnerTipoDAO()
    return resultado.insPartnerTipo(request.json)


@app.route("/updPartnerTipo", methods=["POST"])
def updPartnerTipo():
    resultado = partnertipoDAO.PartnerTipoDAO()
    return resultado.updPartnerTipo(request.json)


@app.route("/delPartnerTipo", methods=["POST"])
def delPartnerTipo():
    resultado = partnertipoDAO.PartnerTipoDAO()
    return resultado.delPartnerTipo(request.json)


"""
  Fim rota: PartnerTipo
"""

"""
  Rotas do WebService para a classe: PartnerStatusVW (VW01135)
"""
import partnerstatusvwDAO


@app.route("/listPartnerStatusVW/", methods=["POST"])
def listPartnerStatusVW():
    resultado = partnerstatusvwDAO.PartnerStatusVWDAO()
    return resultado.listPartnerStatusVW(request.json)


@app.route("/dictPartnerStatusVW/", methods=["POST"])
def dictPartnerStatusVW():
    resultado = partnerstatusvwDAO.PartnerStatusVWDAO()
    return resultado.dictPartnerStatusVW(request.json)


@app.route("/fieldsPartnerStatusVW/", methods=["POST"])
def fieldsPartnerStatusVW():
    resultado = partnerstatusvwDAO.PartnerStatusVWDAO()
    return resultado.fieldsPartnerStatusVW(request.json)


@app.route("/findPartnerStatusVW/", methods=["POST"])
def findPartnerStatusVW():
    resultado = partnerstatusvwDAO.PartnerStatusVWDAO()
    return resultado.findPartnerStatusVW(request.json)


"""
  Fim rota: PartnerStatusVW
"""

"""
  Rotas do WebService para a classe: PartnerTipoVW (VW01136)
"""
import partnertipovwDAO


@app.route("/listPartnerTipoVW/", methods=["POST"])
def listPartnerTipoVW():
    resultado = partnertipovwDAO.PartnerTipoVWDAO()
    return resultado.listPartnerTipoVW(request.json)


@app.route("/dictPartnerTipoVW/", methods=["POST"])
def dictPartnerTipoVW():
    resultado = partnertipovwDAO.PartnerTipoVWDAO()
    return resultado.dictPartnerTipoVW(request.json)


@app.route("/fieldsPartnerTipoVW/", methods=["POST"])
def fieldsPartnerTipoVW():
    resultado = partnertipovwDAO.PartnerTipoVWDAO()
    return resultado.fieldsPartnerTipoVW(request.json)


@app.route("/findPartnerTipoVW/", methods=["POST"])
def findPartnerTipoVW():
    resultado = partnertipovwDAO.PartnerTipoVWDAO()
    return resultado.findPartnerTipoVW(request.json)


"""
  Fim rota: PartnerTipoVW
"""

"""
  Rotas do WebService para a classe: PartnerWorkflowVW (VW01137)
"""
import partnerworkflowvwDAO


@app.route("/listPartnerWorkflowVW/", methods=["POST"])
def listPartnerWorkflowVW():
    resultado = partnerworkflowvwDAO.PartnerWorkflowVWDAO()
    return resultado.listPartnerWorkflowVW(request.json)


@app.route("/dictPartnerWorkflowVW/", methods=["POST"])
def dictPartnerWorkflowVW():
    resultado = partnerworkflowvwDAO.PartnerWorkflowVWDAO()
    return resultado.dictPartnerWorkflowVW(request.json)


@app.route("/fieldsPartnerWorkflowVW/", methods=["POST"])
def fieldsPartnerWorkflowVW():
    resultado = partnerworkflowvwDAO.PartnerWorkflowVWDAO()
    return resultado.fieldsPartnerWorkflowVW(request.json)


@app.route("/findPartnerWorkflowVW/", methods=["POST"])
def findPartnerWorkflowVW():
    resultado = partnerworkflowvwDAO.PartnerWorkflowVWDAO()
    return resultado.findPartnerWorkflowVW(request.json)


"""
  Fim rota: PartnerWorkflowVW
"""

"""
  Rotas do WebService para a classe: ClienteCondicao (TB01153)
"""
import clientecondicaoDAO


@app.route("/listClienteCondicao/", methods=["POST"])
def listClienteCondicao():
    resultado = clientecondicaoDAO.ClienteCondicaoDAO()
    return resultado.listClienteCondicao(request.json)


@app.route("/dictClienteCondicao/", methods=["POST"])
def dictClienteCondicao():
    resultado = clientecondicaoDAO.ClienteCondicaoDAO()
    return resultado.dictClienteCondicao(request.json)


@app.route("/fieldsClienteCondicao/", methods=["POST"])
def fieldsClienteCondicao():
    resultado = clientecondicaoDAO.ClienteCondicaoDAO()
    return resultado.fieldsClienteCondicao(request.json)


@app.route("/findClienteCondicao/", methods=["POST"])
def findClienteCondicao():
    resultado = clientecondicaoDAO.ClienteCondicaoDAO()
    return resultado.findClienteCondicao(request.json)


@app.route("/insClienteCondicao", methods=["POST"])
def insClienteCondicao():
    resultado = clientecondicaoDAO.ClienteCondicaoDAO()
    return resultado.insClienteCondicao(request.json)


@app.route("/updClienteCondicao", methods=["POST"])
def updClienteCondicao():
    resultado = clientecondicaoDAO.ClienteCondicaoDAO()
    return resultado.updClienteCondicao(request.json)


@app.route("/delClienteCondicao", methods=["POST"])
def delClienteCondicao():
    resultado = clientecondicaoDAO.ClienteCondicaoDAO()
    return resultado.delClienteCondicao(request.json)


"""
  Fim rota: ClienteCondicao
"""

"""
  Rotas do WebService para a classe: Partner (TB02300)
"""
import partnerDAO


@app.route("/listPartner/", methods=["POST"])
def listPartner():
    resultado = partnerDAO.PartnerDAO()
    return resultado.listPartner(request.json)


@app.route("/dictPartner/", methods=["POST"])
def dictPartner():
    resultado = partnerDAO.PartnerDAO()
    return resultado.dictPartner(request.json)


@app.route("/fieldsPartner/", methods=["POST"])
def fieldsPartner():
    resultado = partnerDAO.PartnerDAO()
    return resultado.fieldsPartner(request.json)


@app.route("/findPartner/", methods=["POST"])
def findPartner():
    resultado = partnerDAO.PartnerDAO()
    return resultado.findPartner(request.json)


@app.route("/PartnerID", methods=["POST"])
def partnerID():
    resultado = partnerDAO.PartnerDAO()
    return resultado.partnerID(request.json)


@app.route("/insPartner", methods=["POST"])
def insPartner():
    resultado = partnerDAO.PartnerDAO()
    return resultado.insPartner(request.json)


@app.route("/updPartner", methods=["POST"])
def updPartner():
    resultado = partnerDAO.PartnerDAO()
    return resultado.updPartner(request.json)


@app.route("/delPartner", methods=["POST"])
def delPartner():
    resultado = partnerDAO.PartnerDAO()
    return resultado.delPartner(request.json)


"""
  Fim rota: Partner
"""

"""
  Rotas do WebService para a classe: PartnerVW (VW02306)
"""
import partnervwDAO


@app.route("/listPartnerVW/", methods=["POST"])
def listPartnerVW():
    resultado = partnervwDAO.PartnerVWDAO()
    return resultado.listPartnerVW(request.json)


@app.route("/dictPartnerVW/", methods=["POST"])
def dictPartnerVW():
    resultado = partnervwDAO.PartnerVWDAO()
    return resultado.dictPartnerVW(request.json)


@app.route("/fieldsPartnerVW/", methods=["POST"])
def fieldsPartnerVW():
    resultado = partnervwDAO.PartnerVWDAO()
    return resultado.fieldsPartnerVW(request.json)


@app.route("/findPartnerVW/", methods=["POST"])
def findPartnerVW():
    resultado = partnervwDAO.PartnerVWDAO()
    return resultado.findPartnerVW(request.json)


"""
  Fim rota: PartnerVW
"""

"""
  Rotas do WebService para a classe: PartnerItem (TB02301)
"""
import partneritemDAO


@app.route("/listPartnerItem/", methods=["POST"])
def listPartnerItem():
    resultado = partneritemDAO.PartnerItemDAO()
    return resultado.listPartnerItem(request.json)


@app.route("/dictPartnerItem/", methods=["POST"])
def dictPartnerItem():
    resultado = partneritemDAO.PartnerItemDAO()
    return resultado.dictPartnerItem(request.json)


@app.route("/fieldsPartnerItem/", methods=["POST"])
def fieldsPartnerItem():
    resultado = partneritemDAO.PartnerItemDAO()
    return resultado.fieldsPartnerItem(request.json)


@app.route("/findPartnerItem/", methods=["POST"])
def findPartnerItem():
    resultado = partneritemDAO.PartnerItemDAO()
    return resultado.findPartnerItem(request.json)


@app.route("/insPartnerItem", methods=["POST"])
def insPartnerItem():
    resultado = partneritemDAO.PartnerItemDAO()
    return resultado.insPartnerItem(request.json)


@app.route("/updPartnerItem", methods=["POST"])
def updPartnerItem():
    resultado = partneritemDAO.PartnerItemDAO()
    return resultado.updPartnerItem(request.json)


@app.route("/delPartnerItem", methods=["POST"])
def delPartnerItem():
    resultado = partneritemDAO.PartnerItemDAO()
    return resultado.delPartnerItem(request.json)


"""
  Fim rota: PartnerItem
"""

"""
  Rotas do WebService para a classe: PartnerItemVW (VW02307)
"""
import partneritemvwDAO


@app.route("/listPartnerItemVW/", methods=["POST"])
def listPartnerItemVW():
    resultado = partneritemvwDAO.PartnerItemVWDAO()
    return resultado.listPartnerItemVW(request.json)


@app.route("/dictPartnerItemVW/", methods=["POST"])
def dictPartnerItemVW():
    resultado = partneritemvwDAO.PartnerItemVWDAO()
    return resultado.dictPartnerItemVW(request.json)


@app.route("/fieldsPartnerItemVW/", methods=["POST"])
def fieldsPartnerItemVW():
    resultado = partneritemvwDAO.PartnerItemVWDAO()
    return resultado.fieldsPartnerItemVW(request.json)


@app.route("/findPartnerItemVW/", methods=["POST"])
def findPartnerItemVW():
    resultado = partneritemvwDAO.PartnerItemVWDAO()
    return resultado.findPartnerItemVW(request.json)


"""
  Fim rota: PartnerItemVW
"""

"""
  Rotas do WebService para a classe: PartnerHistorico (TB02302)
"""
import partnerhistoricoDAO


@app.route("/listPartnerHistorico/", methods=["POST"])
def listPartnerHistorico():
    resultado = partnerhistoricoDAO.PartnerHistoricoDAO()
    return resultado.listPartnerHistorico(request.json)


@app.route("/dictPartnerHistorico/", methods=["POST"])
def dictPartnerHistorico():
    resultado = partnerhistoricoDAO.PartnerHistoricoDAO()
    return resultado.dictPartnerHistorico(request.json)


@app.route("/fieldsPartnerHistorico/", methods=["POST"])
def fieldsPartnerHistorico():
    resultado = partnerhistoricoDAO.PartnerHistoricoDAO()
    return resultado.fieldsPartnerHistorico(request.json)


@app.route("/findPartnerHistorico/", methods=["POST"])
def findPartnerHistorico():
    resultado = partnerhistoricoDAO.PartnerHistoricoDAO()
    return resultado.findPartnerHistorico(request.json)


@app.route("/insPartnerHistorico", methods=["POST"])
def insPartnerHistorico():
    resultado = partnerhistoricoDAO.PartnerHistoricoDAO()
    return resultado.insPartnerHistorico(request.json)


@app.route("/updPartnerHistorico", methods=["POST"])
def updPartnerHistorico():
    resultado = partnerhistoricoDAO.PartnerHistoricoDAO()
    return resultado.updPartnerHistorico(request.json)


@app.route("/delPartnerHistorico", methods=["POST"])
def delPartnerHistorico():
    resultado = partnerhistoricoDAO.PartnerHistoricoDAO()
    return resultado.delPartnerHistorico(request.json)


"""
  Fim rota: PartnerHistorico
"""

"""
  Rotas do WebService para a classe: PartnerHistoricoVW (VW02308)
"""
import partnerhistoricovwDAO


@app.route("/listPartnerHistoricoVW/", methods=["POST"])
def listPartnerHistoricoVW():
    resultado = partnerhistoricovwDAO.PartnerHistoricoVWDAO()
    return resultado.listPartnerHistoricoVW(request.json)


@app.route("/dictPartnerHistoricoVW/", methods=["POST"])
def dictPartnerHistoricoVW():
    resultado = partnerhistoricovwDAO.PartnerHistoricoVWDAO()
    return resultado.dictPartnerHistoricoVW(request.json)


@app.route("/fieldsPartnerHistoricoVW/", methods=["POST"])
def fieldsPartnerHistoricoVW():
    resultado = partnerhistoricovwDAO.PartnerHistoricoVWDAO()
    return resultado.fieldsPartnerHistoricoVW(request.json)


@app.route("/findPartnerHistoricoVW/", methods=["POST"])
def findPartnerHistoricoVW():
    resultado = partnerhistoricovwDAO.PartnerHistoricoVWDAO()
    return resultado.findPartnerHistoricoVW(request.json)


"""
  Fim rota: PartnerHistoricoVW
"""

"""
  Rotas do WebService para a classe: ClienteCondicaoVW (VW01138)
"""
import clientecondicaovwDAO


@app.route("/listClienteCondicaoVW/", methods=["POST"])
def listClienteCondicaoVW():
    resultado = clientecondicaovwDAO.ClienteCondicaoVWDAO()
    return resultado.listClienteCondicaoVW(request.json)


@app.route("/dictClienteCondicaoVW/", methods=["POST"])
def dictClienteCondicaoVW():
    resultado = clientecondicaovwDAO.ClienteCondicaoVWDAO()
    return resultado.dictClienteCondicaoVW(request.json)


@app.route("/fieldsClienteCondicaoVW/", methods=["POST"])
def fieldsClienteCondicaoVW():
    resultado = clientecondicaovwDAO.ClienteCondicaoVWDAO()
    return resultado.fieldsClienteCondicaoVW(request.json)


@app.route("/findClienteCondicaoVW/", methods=["POST"])
def findClienteCondicaoVW():
    resultado = clientecondicaovwDAO.ClienteCondicaoVWDAO()
    return resultado.findClienteCondicaoVW(request.json)


"""
  Fim rota: ClienteCondicaoVW
"""

"""
  Rotas do WebService para a classe: PartnerReceber (TB04055)
"""
import partnerreceberDAO


@app.route("/listPartnerReceber/", methods=["POST"])
def listPartnerReceber():
    resultado = partnerreceberDAO.PartnerReceberDAO()
    return resultado.listPartnerReceber(request.json)


@app.route("/dictPartnerReceber/", methods=["POST"])
def dictPartnerReceber():
    resultado = partnerreceberDAO.PartnerReceberDAO()
    return resultado.dictPartnerReceber(request.json)


@app.route("/fieldsPartnerReceber/", methods=["POST"])
def fieldsPartnerReceber():
    resultado = partnerreceberDAO.PartnerReceberDAO()
    return resultado.fieldsPartnerReceber(request.json)


@app.route("/findPartnerReceber/", methods=["POST"])
def findPartnerReceber():
    resultado = partnerreceberDAO.PartnerReceberDAO()
    return resultado.findPartnerReceber(request.json)


@app.route("/PartnerReceberID", methods=["POST"])
def partnerreceberID():
    resultado = partnerreceberDAO.PartnerReceberDAO()
    return resultado.partnerreceberID(request.json)


@app.route("/insPartnerReceber", methods=["POST"])
def insPartnerReceber():
    resultado = partnerreceberDAO.PartnerReceberDAO()
    return resultado.insPartnerReceber(request.json)


@app.route("/updPartnerReceber", methods=["POST"])
def updPartnerReceber():
    resultado = partnerreceberDAO.PartnerReceberDAO()
    return resultado.updPartnerReceber(request.json)


@app.route("/delPartnerReceber", methods=["POST"])
def delPartnerReceber():
    resultado = partnerreceberDAO.PartnerReceberDAO()
    return resultado.delPartnerReceber(request.json)


"""
  Fim rota: PartnerReceber
"""

"""
  Rotas do WebService para a classe: PartnerReceberVW (VW04055)
"""
import partnerrecebervwDAO


@app.route("/listPartnerReceberVW/", methods=["POST"])
def listPartnerReceberVW():
    resultado = partnerrecebervwDAO.PartnerReceberVWDAO()
    return resultado.listPartnerReceberVW(request.json)


@app.route("/dictPartnerReceberVW/", methods=["POST"])
def dictPartnerReceberVW():
    resultado = partnerrecebervwDAO.PartnerReceberVWDAO()
    return resultado.dictPartnerReceberVW(request.json)


@app.route("/fieldsPartnerReceberVW/", methods=["POST"])
def fieldsPartnerReceberVW():
    resultado = partnerrecebervwDAO.PartnerReceberVWDAO()
    return resultado.fieldsPartnerReceberVW(request.json)


@app.route("/findPartnerReceberVW/", methods=["POST"])
def findPartnerReceberVW():
    resultado = partnerrecebervwDAO.PartnerReceberVWDAO()
    return resultado.findPartnerReceberVW(request.json)


"""
  Fim rota: PartnerReceberVW
"""

"""
  Rotas do WebService para a classe: ServicoContratado (TB01080)
"""
import servicocontratadoDAO


@app.route("/listServicoContratado/", methods=["POST"])
def listServicoContratado():
    resultado = servicocontratadoDAO.ServicoContratadoDAO()
    return resultado.listServicoContratado(request.json)


@app.route("/dictServicoContratado/", methods=["POST"])
def dictServicoContratado():
    resultado = servicocontratadoDAO.ServicoContratadoDAO()
    return resultado.dictServicoContratado(request.json)


@app.route("/fieldsServicoContratado/", methods=["POST"])
def fieldsServicoContratado():
    resultado = servicocontratadoDAO.ServicoContratadoDAO()
    return resultado.fieldsServicoContratado(request.json)


@app.route("/findServicoContratado/", methods=["POST"])
def findServicoContratado():
    resultado = servicocontratadoDAO.ServicoContratadoDAO()
    return resultado.findServicoContratado(request.json)


@app.route("/ServicoContratadoID", methods=["POST"])
def servicocontratadoID():
    resultado = servicocontratadoDAO.ServicoContratadoDAO()
    return resultado.servicocontratadoID(request.json)


@app.route("/insServicoContratado", methods=["POST"])
def insServicoContratado():
    resultado = servicocontratadoDAO.ServicoContratadoDAO()
    return resultado.insServicoContratado(request.json)


@app.route("/updServicoContratado", methods=["POST"])
def updServicoContratado():
    resultado = servicocontratadoDAO.ServicoContratadoDAO()
    return resultado.updServicoContratado(request.json)


@app.route("/delServicoContratado", methods=["POST"])
def delServicoContratado():
    resultado = servicocontratadoDAO.ServicoContratadoDAO()
    return resultado.delServicoContratado(request.json)


"""
  Fim rota: ServicoContratado
"""

"""
  Rotas do WebService para a classe: ClienteContrato (TB01081)
"""
import clientecontratoDAO


@app.route("/listClienteContrato/", methods=["POST"])
def listClienteContrato():
    resultado = clientecontratoDAO.ClienteContratoDAO()
    return resultado.listClienteContrato(request.json)


@app.route("/dictClienteContrato/", methods=["POST"])
def dictClienteContrato():
    resultado = clientecontratoDAO.ClienteContratoDAO()
    return resultado.dictClienteContrato(request.json)


@app.route("/fieldsClienteContrato/", methods=["POST"])
def fieldsClienteContrato():
    resultado = clientecontratoDAO.ClienteContratoDAO()
    return resultado.fieldsClienteContrato(request.json)


@app.route("/findClienteContrato/", methods=["POST"])
def findClienteContrato():
    resultado = clientecontratoDAO.ClienteContratoDAO()
    return resultado.findClienteContrato(request.json)


@app.route("/insClienteContrato", methods=["POST"])
def insClienteContrato():
    resultado = clientecontratoDAO.ClienteContratoDAO()
    return resultado.insClienteContrato(request.json)


@app.route("/updClienteContrato", methods=["POST"])
def updClienteContrato():
    resultado = clientecontratoDAO.ClienteContratoDAO()
    return resultado.updClienteContrato(request.json)


@app.route("/delClienteContrato", methods=["POST"])
def delClienteContrato():
    resultado = clientecontratoDAO.ClienteContratoDAO()
    return resultado.delClienteContrato(request.json)


"""
  Fim rota: ClienteContrato
"""

"""
  Rotas do WebService para a classe: PartnerBrowseVW (VW01139)
"""
import partnerbrowsevwDAO


@app.route("/listPartnerBrowseVW/", methods=["POST"])
def listPartnerBrowseVW():
    resultado = partnerbrowsevwDAO.PartnerBrowseVWDAO()
    return resultado.listPartnerBrowseVW(request.json)


@app.route("/dictPartnerBrowseVW/", methods=["POST"])
def dictPartnerBrowseVW():
    resultado = partnerbrowsevwDAO.PartnerBrowseVWDAO()
    return resultado.dictPartnerBrowseVW(request.json)


@app.route("/fieldsPartnerBrowseVW/", methods=["POST"])
def fieldsPartnerBrowseVW():
    resultado = partnerbrowsevwDAO.PartnerBrowseVWDAO()
    return resultado.fieldsPartnerBrowseVW(request.json)


@app.route("/findPartnerBrowseVW/", methods=["POST"])
def findPartnerBrowseVW():
    resultado = partnerbrowsevwDAO.PartnerBrowseVWDAO()
    return resultado.findPartnerBrowseVW(request.json)


"""
  Fim rota: PartnerBrowseVW
"""

"""
  Rotas do WebService para a classe: PartnerParceiroVW (VW01140)
"""
import partnerparceirovwDAO


@app.route("/listPartnerParceiroVW/", methods=["POST"])
def listPartnerParceiroVW():
    resultado = partnerparceirovwDAO.PartnerParceiroVWDAO()
    return resultado.listPartnerParceiroVW(request.json)


@app.route("/dictPartnerParceiroVW/", methods=["POST"])
def dictPartnerParceiroVW():
    resultado = partnerparceirovwDAO.PartnerParceiroVWDAO()
    return resultado.dictPartnerParceiroVW(request.json)


@app.route("/fieldsPartnerParceiroVW/", methods=["POST"])
def fieldsPartnerParceiroVW():
    resultado = partnerparceirovwDAO.PartnerParceiroVWDAO()
    return resultado.fieldsPartnerParceiroVW(request.json)


@app.route("/findPartnerParceiroVW/", methods=["POST"])
def findPartnerParceiroVW():
    resultado = partnerparceirovwDAO.PartnerParceiroVWDAO()
    return resultado.findPartnerParceiroVW(request.json)


"""
  Fim rota: PartnerParceiroVW
"""

"""
  Rotas do WebService para a classe: PartnerPainelVW (VW02309)
"""
import partnerpainelvwDAO


@app.route("/listPartnerPainelVW/", methods=["POST"])
def listPartnerPainelVW():
    resultado = partnerpainelvwDAO.PartnerPainelVWDAO()
    return resultado.listPartnerPainelVW(request.json)


@app.route("/dictPartnerPainelVW/", methods=["POST"])
def dictPartnerPainelVW():
    resultado = partnerpainelvwDAO.PartnerPainelVWDAO()
    return resultado.dictPartnerPainelVW(request.json)


@app.route("/fieldsPartnerPainelVW/", methods=["POST"])
def fieldsPartnerPainelVW():
    resultado = partnerpainelvwDAO.PartnerPainelVWDAO()
    return resultado.fieldsPartnerPainelVW(request.json)


@app.route("/findPartnerPainelVW/", methods=["POST"])
def findPartnerPainelVW():
    resultado = partnerpainelvwDAO.PartnerPainelVWDAO()
    return resultado.findPartnerPainelVW(request.json)


"""
  Fim rota: PartnerPainelVW
"""

"""
  Rotas do WebService para a classe: TipoRecebimento (TB04003)
"""
import tiporecebimentoDAO


@app.route("/listTipoRecebimento/", methods=["POST"])
def listTipoRecebimento():
    resultado = tiporecebimentoDAO.TipoRecebimentoDAO()
    return resultado.listTipoRecebimento(request.json)


@app.route("/dictTipoRecebimento/", methods=["POST"])
def dictTipoRecebimento():
    resultado = tiporecebimentoDAO.TipoRecebimentoDAO()
    return resultado.dictTipoRecebimento(request.json)


@app.route("/fieldsTipoRecebimento/", methods=["POST"])
def fieldsTipoRecebimento():
    resultado = tiporecebimentoDAO.TipoRecebimentoDAO()
    return resultado.fieldsTipoRecebimento(request.json)


@app.route("/findTipoRecebimento/", methods=["POST"])
def findTipoRecebimento():
    resultado = tiporecebimentoDAO.TipoRecebimentoDAO()
    return resultado.findTipoRecebimento(request.json)


@app.route("/TipoRecebimentoID", methods=["POST"])
def tiporecebimentoID():
    resultado = tiporecebimentoDAO.TipoRecebimentoDAO()
    return resultado.tiporecebimentoID(request.json)


@app.route("/insTipoRecebimento", methods=["POST"])
def insTipoRecebimento():
    resultado = tiporecebimentoDAO.TipoRecebimentoDAO()
    return resultado.insTipoRecebimento(request.json)


@app.route("/updTipoRecebimento", methods=["POST"])
def updTipoRecebimento():
    resultado = tiporecebimentoDAO.TipoRecebimentoDAO()
    return resultado.updTipoRecebimento(request.json)


@app.route("/delTipoRecebimento", methods=["POST"])
def delTipoRecebimento():
    resultado = tiporecebimentoDAO.TipoRecebimentoDAO()
    return resultado.delTipoRecebimento(request.json)


"""
  Fim rota: TipoRecebimento
"""

"""
  Rotas do WebService para a classe: PartnerParcelaVW (VW04056)
"""
import partnerparcelavwDAO


@app.route("/listPartnerParcelaVW/", methods=["POST"])
def listPartnerParcelaVW():
    resultado = partnerparcelavwDAO.PartnerParcelaVWDAO()
    return resultado.listPartnerParcelaVW(request.json)


@app.route("/dictPartnerParcelaVW/", methods=["POST"])
def dictPartnerParcelaVW():
    resultado = partnerparcelavwDAO.PartnerParcelaVWDAO()
    return resultado.dictPartnerParcelaVW(request.json)


@app.route("/fieldsPartnerParcelaVW/", methods=["POST"])
def fieldsPartnerParcelaVW():
    resultado = partnerparcelavwDAO.PartnerParcelaVWDAO()
    return resultado.fieldsPartnerParcelaVW(request.json)


@app.route("/findPartnerParcelaVW/", methods=["POST"])
def findPartnerParcelaVW():
    resultado = partnerparcelavwDAO.PartnerParcelaVWDAO()
    return resultado.findPartnerParcelaVW(request.json)


"""
  Fim rota: PartnerParcelaVW
"""

"""
  Rotas do WebService para a classe: OportunidadeTipoStatus (TB01154)
"""
import oportunidadetipostatusDAO


@app.route("/listOportunidadeTipoStatus/", methods=["POST"])
def listOportunidadeTipoStatus():
    resultado = oportunidadetipostatusDAO.OportunidadeTipoStatusDAO()
    return resultado.listOportunidadeTipoStatus(request.json)


@app.route("/dictOportunidadeTipoStatus/", methods=["POST"])
def dictOportunidadeTipoStatus():
    resultado = oportunidadetipostatusDAO.OportunidadeTipoStatusDAO()
    return resultado.dictOportunidadeTipoStatus(request.json)


@app.route("/fieldsOportunidadeTipoStatus/", methods=["POST"])
def fieldsOportunidadeTipoStatus():
    resultado = oportunidadetipostatusDAO.OportunidadeTipoStatusDAO()
    return resultado.fieldsOportunidadeTipoStatus(request.json)


@app.route("/findOportunidadeTipoStatus/", methods=["POST"])
def findOportunidadeTipoStatus():
    resultado = oportunidadetipostatusDAO.OportunidadeTipoStatusDAO()
    return resultado.findOportunidadeTipoStatus(request.json)


@app.route("/insOportunidadeTipoStatus", methods=["POST"])
def insOportunidadeTipoStatus():
    resultado = oportunidadetipostatusDAO.OportunidadeTipoStatusDAO()
    return resultado.insOportunidadeTipoStatus(request.json)


@app.route("/updOportunidadeTipoStatus", methods=["POST"])
def updOportunidadeTipoStatus():
    resultado = oportunidadetipostatusDAO.OportunidadeTipoStatusDAO()
    return resultado.updOportunidadeTipoStatus(request.json)


@app.route("/delOportunidadeTipoStatus", methods=["POST"])
def delOportunidadeTipoStatus():
    resultado = oportunidadetipostatusDAO.OportunidadeTipoStatusDAO()
    return resultado.delOportunidadeTipoStatus(request.json)


"""
  Fim rota: OportunidadeTipoStatus
"""

"""
  Rotas do WebService para a classe: OportunidadeTipoStatusVW (VW01141)
"""
import oportunidadetipostatusvwDAO


@app.route("/listOportunidadeTipoStatusVW/", methods=["POST"])
def listOportunidadeTipoStatusVW():
    resultado = oportunidadetipostatusvwDAO.OportunidadeTipoStatusVWDAO()
    return resultado.listOportunidadeTipoStatusVW(request.json)


@app.route("/dictOportunidadeTipoStatusVW/", methods=["POST"])
def dictOportunidadeTipoStatusVW():
    resultado = oportunidadetipostatusvwDAO.OportunidadeTipoStatusVWDAO()
    return resultado.dictOportunidadeTipoStatusVW(request.json)


@app.route("/fieldsOportunidadeTipoStatusVW/", methods=["POST"])
def fieldsOportunidadeTipoStatusVW():
    resultado = oportunidadetipostatusvwDAO.OportunidadeTipoStatusVWDAO()
    return resultado.fieldsOportunidadeTipoStatusVW(request.json)


@app.route("/findOportunidadeTipoStatusVW/", methods=["POST"])
def findOportunidadeTipoStatusVW():
    resultado = oportunidadetipostatusvwDAO.OportunidadeTipoStatusVWDAO()
    return resultado.findOportunidadeTipoStatusVW(request.json)


"""
  Fim rota: OportunidadeTipoStatusVW
"""

"""
  Rotas do WebService para a classe: PrecontratoTipoStatus (TB01155)
"""
import precontratotipostatusDAO


@app.route("/listPrecontratoTipoStatus/", methods=["POST"])
def listPrecontratoTipoStatus():
    resultado = precontratotipostatusDAO.PrecontratoTipoStatusDAO()
    return resultado.listPrecontratoTipoStatus(request.json)


@app.route("/dictPrecontratoTipoStatus/", methods=["POST"])
def dictPrecontratoTipoStatus():
    resultado = precontratotipostatusDAO.PrecontratoTipoStatusDAO()
    return resultado.dictPrecontratoTipoStatus(request.json)


@app.route("/fieldsPrecontratoTipoStatus/", methods=["POST"])
def fieldsPrecontratoTipoStatus():
    resultado = precontratotipostatusDAO.PrecontratoTipoStatusDAO()
    return resultado.fieldsPrecontratoTipoStatus(request.json)


@app.route("/findPrecontratoTipoStatus/", methods=["POST"])
def findPrecontratoTipoStatus():
    resultado = precontratotipostatusDAO.PrecontratoTipoStatusDAO()
    return resultado.findPrecontratoTipoStatus(request.json)


@app.route("/insPrecontratoTipoStatus", methods=["POST"])
def insPrecontratoTipoStatus():
    resultado = precontratotipostatusDAO.PrecontratoTipoStatusDAO()
    return resultado.insPrecontratoTipoStatus(request.json)


@app.route("/updPrecontratoTipoStatus", methods=["POST"])
def updPrecontratoTipoStatus():
    resultado = precontratotipostatusDAO.PrecontratoTipoStatusDAO()
    return resultado.updPrecontratoTipoStatus(request.json)


@app.route("/delPrecontratoTipoStatus", methods=["POST"])
def delPrecontratoTipoStatus():
    resultado = precontratotipostatusDAO.PrecontratoTipoStatusDAO()
    return resultado.delPrecontratoTipoStatus(request.json)


"""
  Fim rota: PrecontratoTipoStatus
"""

"""
  Rotas do WebService para a classe: PrecontratoTipoStatusVW (VW01142)
"""
import precontratotipostatusvwDAO


@app.route("/listPrecontratoTipoStatusVW/", methods=["POST"])
def listPrecontratoTipoStatusVW():
    resultado = precontratotipostatusvwDAO.PrecontratoTipoStatusVWDAO()
    return resultado.listPrecontratoTipoStatusVW(request.json)


@app.route("/dictPrecontratoTipoStatusVW/", methods=["POST"])
def dictPrecontratoTipoStatusVW():
    resultado = precontratotipostatusvwDAO.PrecontratoTipoStatusVWDAO()
    return resultado.dictPrecontratoTipoStatusVW(request.json)


@app.route("/fieldsPrecontratoTipoStatusVW/", methods=["POST"])
def fieldsPrecontratoTipoStatusVW():
    resultado = precontratotipostatusvwDAO.PrecontratoTipoStatusVWDAO()
    return resultado.fieldsPrecontratoTipoStatusVW(request.json)


@app.route("/findPrecontratoTipoStatusVW/", methods=["POST"])
def findPrecontratoTipoStatusVW():
    resultado = precontratotipostatusvwDAO.PrecontratoTipoStatusVWDAO()
    return resultado.findPrecontratoTipoStatusVW(request.json)


"""
  Fim rota: PrecontratoTipoStatusVW
"""

"""
  Rotas do WebService para a classe: OportunidadePainelVW (VW02313)
"""
import oportunidadepainelvwDAO


@app.route("/listOportunidadePainelVW/", methods=["POST"])
def listOportunidadePainelVW():
    resultado = oportunidadepainelvwDAO.OportunidadePainelVWDAO()
    return resultado.listOportunidadePainelVW(request.json)


@app.route("/dictOportunidadePainelVW/", methods=["POST"])
def dictOportunidadePainelVW():
    resultado = oportunidadepainelvwDAO.OportunidadePainelVWDAO()
    return resultado.dictOportunidadePainelVW(request.json)


@app.route("/fieldsOportunidadePainelVW/", methods=["POST"])
def fieldsOportunidadePainelVW():
    resultado = oportunidadepainelvwDAO.OportunidadePainelVWDAO()
    return resultado.fieldsOportunidadePainelVW(request.json)


@app.route("/findOportunidadePainelVW/", methods=["POST"])
def findOportunidadePainelVW():
    resultado = oportunidadepainelvwDAO.OportunidadePainelVWDAO()
    return resultado.findOportunidadePainelVW(request.json)


"""
  Fim rota: OportunidadePainelVW
"""

"""
  Rotas do WebService para a classe: PrecontratoPainelVW (VW02314)
"""
import precontratopainelvwDAO


@app.route("/listPrecontratoPainelVW/", methods=["POST"])
def listPrecontratoPainelVW():
    resultado = precontratopainelvwDAO.PrecontratoPainelVWDAO()
    return resultado.listPrecontratoPainelVW(request.json)


@app.route("/dictPrecontratoPainelVW/", methods=["POST"])
def dictPrecontratoPainelVW():
    resultado = precontratopainelvwDAO.PrecontratoPainelVWDAO()
    return resultado.dictPrecontratoPainelVW(request.json)


@app.route("/fieldsPrecontratoPainelVW/", methods=["POST"])
def fieldsPrecontratoPainelVW():
    resultado = precontratopainelvwDAO.PrecontratoPainelVWDAO()
    return resultado.fieldsPrecontratoPainelVW(request.json)


@app.route("/findPrecontratoPainelVW/", methods=["POST"])
def findPrecontratoPainelVW():
    resultado = precontratopainelvwDAO.PrecontratoPainelVWDAO()
    return resultado.findPrecontratoPainelVW(request.json)


"""
  Fim rota: PrecontratoPainelVW
"""

"""
  Rotas do WebService para a classe: DashbordModuleVW (VW00025)
"""
import dashbordmodulevwDAO


@app.route("/listDashbordModuleVW/", methods=["POST"])
def listDashbordModuleVW():
    resultado = dashbordmodulevwDAO.DashbordModuleVWDAO()
    return resultado.listDashbordModuleVW(request.json)


@app.route("/dictDashbordModuleVW/", methods=["POST"])
def dictDashbordModuleVW():
    resultado = dashbordmodulevwDAO.DashbordModuleVWDAO()
    return resultado.dictDashbordModuleVW(request.json)


@app.route("/fieldsDashbordModuleVW/", methods=["POST"])
def fieldsDashbordModuleVW():
    resultado = dashbordmodulevwDAO.DashbordModuleVWDAO()
    return resultado.fieldsDashbordModuleVW(request.json)


@app.route("/findDashbordModuleVW/", methods=["POST"])
def findDashbordModuleVW():
    resultado = dashbordmodulevwDAO.DashbordModuleVWDAO()
    return resultado.findDashbordModuleVW(request.json)


"""
  Fim rota: DashbordModuleVW
"""

"""
  Rotas do WebService para a classe: DashboardOrder (TB00121)
"""
import dashboardorderDAO


@app.route("/listDashboardOrder/", methods=["POST"])
def listDashboardOrder():
    resultado = dashboardorderDAO.DashboardOrderDAO()
    return resultado.listDashboardOrder(request.json)


@app.route("/dictDashboardOrder/", methods=["POST"])
def dictDashboardOrder():
    resultado = dashboardorderDAO.DashboardOrderDAO()
    return resultado.dictDashboardOrder(request.json)


@app.route("/fieldsDashboardOrder/", methods=["POST"])
def fieldsDashboardOrder():
    resultado = dashboardorderDAO.DashboardOrderDAO()
    return resultado.fieldsDashboardOrder(request.json)


@app.route("/findDashboardOrder/", methods=["POST"])
def findDashboardOrder():
    resultado = dashboardorderDAO.DashboardOrderDAO()
    return resultado.findDashboardOrder(request.json)


@app.route("/insDashboardOrder", methods=["POST"])
def insDashboardOrder():
    resultado = dashboardorderDAO.DashboardOrderDAO()
    return resultado.insDashboardOrder(request.json)


@app.route("/updDashboardOrder", methods=["POST"])
def updDashboardOrder():
    resultado = dashboardorderDAO.DashboardOrderDAO()
    return resultado.updDashboardOrder(request.json)


@app.route("/delDashboardOrder", methods=["POST"])
def delDashboardOrder():
    resultado = dashboardorderDAO.DashboardOrderDAO()
    return resultado.delDashboardOrder(request.json)


"""
  Fim rota: DashboardOrder
"""

"""
  Rotas do WebService para a classe: PrecontratoReportVW (VW02315)
"""
import precontratoreportvwDAO


@app.route("/listPrecontratoReportVW/", methods=["POST"])
def listPrecontratoReportVW():
    resultado = precontratoreportvwDAO.PrecontratoReportVWDAO()
    return resultado.listPrecontratoReportVW(request.json)


@app.route("/dictPrecontratoReportVW/", methods=["POST"])
def dictPrecontratoReportVW():
    resultado = precontratoreportvwDAO.PrecontratoReportVWDAO()
    return resultado.dictPrecontratoReportVW(request.json)


@app.route("/fieldsPrecontratoReportVW/", methods=["POST"])
def fieldsPrecontratoReportVW():
    resultado = precontratoreportvwDAO.PrecontratoReportVWDAO()
    return resultado.fieldsPrecontratoReportVW(request.json)


@app.route("/findPrecontratoReportVW/", methods=["POST"])
def findPrecontratoReportVW():
    resultado = precontratoreportvwDAO.PrecontratoReportVWDAO()
    return resultado.findPrecontratoReportVW(request.json)


"""
  Fim rota: PrecontratoReportVW
"""

"""
  Rotas do WebService para a classe: PrecontratoComissaoReportVW (VW02316)
"""
import precontratocomissaoreportvwDAO


@app.route("/listPrecontratoComissaoReportVW/", methods=["POST"])
def listPrecontratoComissaoReportVW():
    resultado = precontratocomissaoreportvwDAO.PrecontratoComissaoReportVWDAO()
    return resultado.listPrecontratoComissaoReportVW(request.json)


@app.route("/dictPrecontratoComissaoReportVW/", methods=["POST"])
def dictPrecontratoComissaoReportVW():
    resultado = precontratocomissaoreportvwDAO.PrecontratoComissaoReportVWDAO()
    return resultado.dictPrecontratoComissaoReportVW(request.json)


@app.route("/fieldsPrecontratoComissaoReportVW/", methods=["POST"])
def fieldsPrecontratoComissaoReportVW():
    resultado = precontratocomissaoreportvwDAO.PrecontratoComissaoReportVWDAO()
    return resultado.fieldsPrecontratoComissaoReportVW(request.json)


@app.route("/findPrecontratoComissaoReportVW/", methods=["POST"])
def findPrecontratoComissaoReportVW():
    resultado = precontratocomissaoreportvwDAO.PrecontratoComissaoReportVWDAO()
    return resultado.findPrecontratoComissaoReportVW(request.json)


"""
  Fim rota: PrecontratoComissaoReportVW
"""

"""
  Rotas do WebService para a classe: PrevendaStatus (TB01156)
"""
import prevendastatusDAO


@app.route("/listPrevendaStatus/", methods=["POST"])
def listPrevendaStatus():
    resultado = prevendastatusDAO.PrevendaStatusDAO()
    return resultado.listPrevendaStatus(request.json)


@app.route("/dictPrevendaStatus/", methods=["POST"])
def dictPrevendaStatus():
    resultado = prevendastatusDAO.PrevendaStatusDAO()
    return resultado.dictPrevendaStatus(request.json)


@app.route("/fieldsPrevendaStatus/", methods=["POST"])
def fieldsPrevendaStatus():
    resultado = prevendastatusDAO.PrevendaStatusDAO()
    return resultado.fieldsPrevendaStatus(request.json)


@app.route("/findPrevendaStatus/", methods=["POST"])
def findPrevendaStatus():
    resultado = prevendastatusDAO.PrevendaStatusDAO()
    return resultado.findPrevendaStatus(request.json)


@app.route("/PrevendaStatusID", methods=["POST"])
def prevendastatusID():
    resultado = prevendastatusDAO.PrevendaStatusDAO()
    return resultado.prevendastatusID(request.json)


@app.route("/insPrevendaStatus", methods=["POST"])
def insPrevendaStatus():
    resultado = prevendastatusDAO.PrevendaStatusDAO()
    return resultado.insPrevendaStatus(request.json)


@app.route("/updPrevendaStatus", methods=["POST"])
def updPrevendaStatus():
    resultado = prevendastatusDAO.PrevendaStatusDAO()
    return resultado.updPrevendaStatus(request.json)


@app.route("/delPrevendaStatus", methods=["POST"])
def delPrevendaStatus():
    resultado = prevendastatusDAO.PrevendaStatusDAO()
    return resultado.delPrevendaStatus(request.json)


"""
  Fim rota: PrevendaStatus
"""

"""
  Rotas do WebService para a classe: PrevendaWorkflow (TB01157)
"""
import prevendaworkflowDAO


@app.route("/listPrevendaWorkflow/", methods=["POST"])
def listPrevendaWorkflow():
    resultado = prevendaworkflowDAO.PrevendaWorkflowDAO()
    return resultado.listPrevendaWorkflow(request.json)


@app.route("/dictPrevendaWorkflow/", methods=["POST"])
def dictPrevendaWorkflow():
    resultado = prevendaworkflowDAO.PrevendaWorkflowDAO()
    return resultado.dictPrevendaWorkflow(request.json)


@app.route("/fieldsPrevendaWorkflow/", methods=["POST"])
def fieldsPrevendaWorkflow():
    resultado = prevendaworkflowDAO.PrevendaWorkflowDAO()
    return resultado.fieldsPrevendaWorkflow(request.json)


@app.route("/findPrevendaWorkflow/", methods=["POST"])
def findPrevendaWorkflow():
    resultado = prevendaworkflowDAO.PrevendaWorkflowDAO()
    return resultado.findPrevendaWorkflow(request.json)


@app.route("/insPrevendaWorkflow", methods=["POST"])
def insPrevendaWorkflow():
    resultado = prevendaworkflowDAO.PrevendaWorkflowDAO()
    return resultado.insPrevendaWorkflow(request.json)


@app.route("/updPrevendaWorkflow", methods=["POST"])
def updPrevendaWorkflow():
    resultado = prevendaworkflowDAO.PrevendaWorkflowDAO()
    return resultado.updPrevendaWorkflow(request.json)


@app.route("/delPrevendaWorkflow", methods=["POST"])
def delPrevendaWorkflow():
    resultado = prevendaworkflowDAO.PrevendaWorkflowDAO()
    return resultado.delPrevendaWorkflow(request.json)


"""
  Fim rota: PrevendaWorkflow
"""

"""
  Rotas do WebService para a classe: PrevendaUser (TB01158)
"""
import prevendauserDAO


@app.route("/listPrevendaUser/", methods=["POST"])
def listPrevendaUser():
    resultado = prevendauserDAO.PrevendaUserDAO()
    return resultado.listPrevendaUser(request.json)


@app.route("/dictPrevendaUser/", methods=["POST"])
def dictPrevendaUser():
    resultado = prevendauserDAO.PrevendaUserDAO()
    return resultado.dictPrevendaUser(request.json)


@app.route("/fieldsPrevendaUser/", methods=["POST"])
def fieldsPrevendaUser():
    resultado = prevendauserDAO.PrevendaUserDAO()
    return resultado.fieldsPrevendaUser(request.json)


@app.route("/findPrevendaUser/", methods=["POST"])
def findPrevendaUser():
    resultado = prevendauserDAO.PrevendaUserDAO()
    return resultado.findPrevendaUser(request.json)


@app.route("/insPrevendaUser", methods=["POST"])
def insPrevendaUser():
    resultado = prevendauserDAO.PrevendaUserDAO()
    return resultado.insPrevendaUser(request.json)


@app.route("/updPrevendaUser", methods=["POST"])
def updPrevendaUser():
    resultado = prevendauserDAO.PrevendaUserDAO()
    return resultado.updPrevendaUser(request.json)


@app.route("/delPrevendaUser", methods=["POST"])
def delPrevendaUser():
    resultado = prevendauserDAO.PrevendaUserDAO()
    return resultado.delPrevendaUser(request.json)


"""
  Fim rota: PrevendaUser
"""

"""
  Rotas do WebService para a classe: PrevendaTipo (TB01160)
"""
import prevendatipoDAO


@app.route("/listPrevendaTipo/", methods=["POST"])
def listPrevendaTipo():
    resultado = prevendatipoDAO.PrevendaTipoDAO()
    return resultado.listPrevendaTipo(request.json)


@app.route("/dictPrevendaTipo/", methods=["POST"])
def dictPrevendaTipo():
    resultado = prevendatipoDAO.PrevendaTipoDAO()
    return resultado.dictPrevendaTipo(request.json)


@app.route("/fieldsPrevendaTipo/", methods=["POST"])
def fieldsPrevendaTipo():
    resultado = prevendatipoDAO.PrevendaTipoDAO()
    return resultado.fieldsPrevendaTipo(request.json)


@app.route("/findPrevendaTipo/", methods=["POST"])
def findPrevendaTipo():
    resultado = prevendatipoDAO.PrevendaTipoDAO()
    return resultado.findPrevendaTipo(request.json)


@app.route("/PrevendaTipoID", methods=["POST"])
def prevendatipoID():
    resultado = prevendatipoDAO.PrevendaTipoDAO()
    return resultado.prevendatipoID(request.json)


@app.route("/insPrevendaTipo", methods=["POST"])
def insPrevendaTipo():
    resultado = prevendatipoDAO.PrevendaTipoDAO()
    return resultado.insPrevendaTipo(request.json)


@app.route("/updPrevendaTipo", methods=["POST"])
def updPrevendaTipo():
    resultado = prevendatipoDAO.PrevendaTipoDAO()
    return resultado.updPrevendaTipo(request.json)


@app.route("/delPrevendaTipo", methods=["POST"])
def delPrevendaTipo():
    resultado = prevendatipoDAO.PrevendaTipoDAO()
    return resultado.delPrevendaTipo(request.json)


"""
  Fim rota: PrevendaTipo
"""

"""
  Rotas do WebService para a classe: PrevendaTipoVW (VW01143)
"""
import prevendatipovwDAO


@app.route("/listPrevendaTipoVW/", methods=["POST"])
def listPrevendaTipoVW():
    resultado = prevendatipovwDAO.PrevendaTipoVWDAO()
    return resultado.listPrevendaTipoVW(request.json)


@app.route("/dictPrevendaTipoVW/", methods=["POST"])
def dictPrevendaTipoVW():
    resultado = prevendatipovwDAO.PrevendaTipoVWDAO()
    return resultado.dictPrevendaTipoVW(request.json)


@app.route("/fieldsPrevendaTipoVW/", methods=["POST"])
def fieldsPrevendaTipoVW():
    resultado = prevendatipovwDAO.PrevendaTipoVWDAO()
    return resultado.fieldsPrevendaTipoVW(request.json)


@app.route("/findPrevendaTipoVW/", methods=["POST"])
def findPrevendaTipoVW():
    resultado = prevendatipovwDAO.PrevendaTipoVWDAO()
    return resultado.findPrevendaTipoVW(request.json)


"""
  Fim rota: PrevendaTipoVW
"""

"""
  Rotas do WebService para a classe: PrevendaWordkflowVW (VW01144)
"""
import prevendawordkflowvwDAO


@app.route("/listPrevendaWordkflowVW/", methods=["POST"])
def listPrevendaWordkflowVW():
    resultado = prevendawordkflowvwDAO.PrevendaWordkflowVWDAO()
    return resultado.listPrevendaWordkflowVW(request.json)


@app.route("/dictPrevendaWordkflowVW/", methods=["POST"])
def dictPrevendaWordkflowVW():
    resultado = prevendawordkflowvwDAO.PrevendaWordkflowVWDAO()
    return resultado.dictPrevendaWordkflowVW(request.json)


@app.route("/fieldsPrevendaWordkflowVW/", methods=["POST"])
def fieldsPrevendaWordkflowVW():
    resultado = prevendawordkflowvwDAO.PrevendaWordkflowVWDAO()
    return resultado.fieldsPrevendaWordkflowVW(request.json)


@app.route("/findPrevendaWordkflowVW/", methods=["POST"])
def findPrevendaWordkflowVW():
    resultado = prevendawordkflowvwDAO.PrevendaWordkflowVWDAO()
    return resultado.findPrevendaWordkflowVW(request.json)


"""
  Fim rota: PrevendaWordkflowVW
"""

"""
  Rotas do WebService para a classe: Prevenda (TB02303)
"""
import prevendaDAO


@app.route("/listPrevenda/", methods=["POST"])
def listPrevenda():
    resultado = prevendaDAO.PrevendaDAO()
    return resultado.listPrevenda(request.json)


@app.route("/dictPrevenda/", methods=["POST"])
def dictPrevenda():
    resultado = prevendaDAO.PrevendaDAO()
    return resultado.dictPrevenda(request.json)


@app.route("/fieldsPrevenda/", methods=["POST"])
def fieldsPrevenda():
    resultado = prevendaDAO.PrevendaDAO()
    return resultado.fieldsPrevenda(request.json)


@app.route("/findPrevenda/", methods=["POST"])
def findPrevenda():
    resultado = prevendaDAO.PrevendaDAO()
    return resultado.findPrevenda(request.json)


@app.route("/PrevendaID", methods=["POST"])
def prevendaID():
    resultado = prevendaDAO.PrevendaDAO()
    return resultado.prevendaID(request.json)


@app.route("/insPrevenda", methods=["POST"])
def insPrevenda():
    resultado = prevendaDAO.PrevendaDAO()
    return resultado.insPrevenda(request.json)


@app.route("/updPrevenda", methods=["POST"])
def updPrevenda():
    resultado = prevendaDAO.PrevendaDAO()
    return resultado.updPrevenda(request.json)


@app.route("/delPrevenda", methods=["POST"])
def delPrevenda():
    resultado = prevendaDAO.PrevendaDAO()
    return resultado.delPrevenda(request.json)


"""
  Fim rota: Prevenda
"""

"""
  Rotas do WebService para a classe: PrevendaVW (VW02317)
"""
import prevendavwDAO


@app.route("/listPrevendaVW/", methods=["POST"])
def listPrevendaVW():
    resultado = prevendavwDAO.PrevendaVWDAO()
    return resultado.listPrevendaVW(request.json)


@app.route("/dictPrevendaVW/", methods=["POST"])
def dictPrevendaVW():
    resultado = prevendavwDAO.PrevendaVWDAO()
    return resultado.dictPrevendaVW(request.json)


@app.route("/fieldsPrevendaVW/", methods=["POST"])
def fieldsPrevendaVW():
    resultado = prevendavwDAO.PrevendaVWDAO()
    return resultado.fieldsPrevendaVW(request.json)


@app.route("/findPrevendaVW/", methods=["POST"])
def findPrevendaVW():
    resultado = prevendavwDAO.PrevendaVWDAO()
    return resultado.findPrevendaVW(request.json)


"""
  Fim rota: PrevendaVW
"""

"""
  Rotas do WebService para a classe: PrevendaItem (TB02304)
"""
import prevendaitemDAO


@app.route("/listPrevendaItem/", methods=["POST"])
def listPrevendaItem():
    resultado = prevendaitemDAO.PrevendaItemDAO()
    return resultado.listPrevendaItem(request.json)


@app.route("/dictPrevendaItem/", methods=["POST"])
def dictPrevendaItem():
    resultado = prevendaitemDAO.PrevendaItemDAO()
    return resultado.dictPrevendaItem(request.json)


@app.route("/fieldsPrevendaItem/", methods=["POST"])
def fieldsPrevendaItem():
    resultado = prevendaitemDAO.PrevendaItemDAO()
    return resultado.fieldsPrevendaItem(request.json)


@app.route("/findPrevendaItem/", methods=["POST"])
def findPrevendaItem():
    resultado = prevendaitemDAO.PrevendaItemDAO()
    return resultado.findPrevendaItem(request.json)


@app.route("/PrevendaItemID", methods=["POST"])
def prevendaitemID():
    resultado = prevendaitemDAO.PrevendaItemDAO()
    return resultado.prevendaitemID(request.json)


@app.route("/insPrevendaItem", methods=["POST"])
def insPrevendaItem():
    resultado = prevendaitemDAO.PrevendaItemDAO()
    return resultado.insPrevendaItem(request.json)


@app.route("/updPrevendaItem", methods=["POST"])
def updPrevendaItem():
    resultado = prevendaitemDAO.PrevendaItemDAO()
    return resultado.updPrevendaItem(request.json)


@app.route("/delPrevendaItem", methods=["POST"])
def delPrevendaItem():
    resultado = prevendaitemDAO.PrevendaItemDAO()
    return resultado.delPrevendaItem(request.json)


"""
  Fim rota: PrevendaItem
"""

"""
  Rotas do WebService para a classe: PrevendaServico (TB02305)
"""
import prevendaservicoDAO


@app.route("/listPrevendaServico/", methods=["POST"])
def listPrevendaServico():
    resultado = prevendaservicoDAO.PrevendaServicoDAO()
    return resultado.listPrevendaServico(request.json)


@app.route("/dictPrevendaServico/", methods=["POST"])
def dictPrevendaServico():
    resultado = prevendaservicoDAO.PrevendaServicoDAO()
    return resultado.dictPrevendaServico(request.json)


@app.route("/fieldsPrevendaServico/", methods=["POST"])
def fieldsPrevendaServico():
    resultado = prevendaservicoDAO.PrevendaServicoDAO()
    return resultado.fieldsPrevendaServico(request.json)


@app.route("/findPrevendaServico/", methods=["POST"])
def findPrevendaServico():
    resultado = prevendaservicoDAO.PrevendaServicoDAO()
    return resultado.findPrevendaServico(request.json)


@app.route("/PrevendaServicoID", methods=["POST"])
def prevendaservicoID():
    resultado = prevendaservicoDAO.PrevendaServicoDAO()
    return resultado.prevendaservicoID(request.json)


@app.route("/insPrevendaServico", methods=["POST"])
def insPrevendaServico():
    resultado = prevendaservicoDAO.PrevendaServicoDAO()
    return resultado.insPrevendaServico(request.json)


@app.route("/updPrevendaServico", methods=["POST"])
def updPrevendaServico():
    resultado = prevendaservicoDAO.PrevendaServicoDAO()
    return resultado.updPrevendaServico(request.json)


@app.route("/delPrevendaServico", methods=["POST"])
def delPrevendaServico():
    resultado = prevendaservicoDAO.PrevendaServicoDAO()
    return resultado.delPrevendaServico(request.json)


"""
  Fim rota: PrevendaServico
"""

"""
  Rotas do WebService para a classe: ProdmovVW (VW00006)
"""
import prodmovvwDAO


@app.route("/listProdmovVW/", methods=["POST"])
def listProdmovVW():
    resultado = prodmovvwDAO.ProdmovVWDAO()
    return resultado.listProdmovVW(request.json)


@app.route("/dictProdmovVW/", methods=["POST"])
def dictProdmovVW():
    resultado = prodmovvwDAO.ProdmovVWDAO()
    return resultado.dictProdmovVW(request.json)


@app.route("/fieldsProdmovVW/", methods=["POST"])
def fieldsProdmovVW():
    resultado = prodmovvwDAO.ProdmovVWDAO()
    return resultado.fieldsProdmovVW(request.json)


@app.route("/findProdmovVW/", methods=["POST"])
def findProdmovVW():
    resultado = prodmovvwDAO.ProdmovVWDAO()
    return resultado.findProdmovVW(request.json)


"""
  Rotas do WebService para a classe: ProdcliVW (VW00002)
"""
import prodclivwDAO


@app.route("/listProdcliVW/", methods=["POST"])
def listProdcliVW():
    resultado = prodclivwDAO.ProdcliVWDAO()
    return resultado.listProdcliVW(request.json)


@app.route("/dictProdcliVW/", methods=["POST"])
def dictProdcliVW():
    resultado = prodclivwDAO.ProdcliVWDAO()
    return resultado.dictProdcliVW(request.json)


@app.route("/fieldsProdcliVW/", methods=["POST"])
def fieldsProdcliVW():
    resultado = prodclivwDAO.ProdcliVWDAO()
    return resultado.fieldsProdcliVW(request.json)


@app.route("/findProdcliVW/", methods=["POST"])
def findProdcliVW():
    resultado = prodclivwDAO.ProdcliVWDAO()
    return resultado.findProdcliVW(request.json)


"""
  Fim rota: ProdcliVW
"""

"""
  Rotas do WebService para a classe: BrowseprodVW (VW00005)
"""
import browseprodvwDAO


@app.route("/listBrowseprodVW/", methods=["POST"])
def listBrowseprodVW():
    resultado = browseprodvwDAO.BrowseprodVWDAO()
    return resultado.listBrowseprodVW(request.json)


@app.route("/dictBrowseprodVW/", methods=["POST"])
def dictBrowseprodVW():
    resultado = browseprodvwDAO.BrowseprodVWDAO()
    return resultado.dictBrowseprodVW(request.json)


@app.route("/fieldsBrowseprodVW/", methods=["POST"])
def fieldsBrowseprodVW():
    resultado = browseprodvwDAO.BrowseprodVWDAO()
    return resultado.fieldsBrowseprodVW(request.json)


@app.route("/findBrowseprodVW/", methods=["POST"])
def findBrowseprodVW():
    resultado = browseprodvwDAO.BrowseprodVWDAO()
    return resultado.findBrowseprodVW(request.json)


"""
  Fim rota: BrowseprodVW
"""

"""
  Rotas do WebService para a classe: PrevendaTipoStatus (TB01161)
"""
import prevendatipostatusDAO


@app.route("/listPrevendaTipoStatus/", methods=["POST"])
def listPrevendaTipoStatus():
    resultado = prevendatipostatusDAO.PrevendaTipoStatusDAO()
    return resultado.listPrevendaTipoStatus(request.json)


@app.route("/dictPrevendaTipoStatus/", methods=["POST"])
def dictPrevendaTipoStatus():
    resultado = prevendatipostatusDAO.PrevendaTipoStatusDAO()
    return resultado.dictPrevendaTipoStatus(request.json)


@app.route("/fieldsPrevendaTipoStatus/", methods=["POST"])
def fieldsPrevendaTipoStatus():
    resultado = prevendatipostatusDAO.PrevendaTipoStatusDAO()
    return resultado.fieldsPrevendaTipoStatus(request.json)


@app.route("/findPrevendaTipoStatus/", methods=["POST"])
def findPrevendaTipoStatus():
    resultado = prevendatipostatusDAO.PrevendaTipoStatusDAO()
    return resultado.findPrevendaTipoStatus(request.json)


@app.route("/PrevendaTipoStatusID", methods=["POST"])
def prevendatipostatusID():
    resultado = prevendatipostatusDAO.PrevendaTipoStatusDAO()
    return resultado.prevendatipostatusID(request.json)


@app.route("/insPrevendaTipoStatus", methods=["POST"])
def insPrevendaTipoStatus():
    resultado = prevendatipostatusDAO.PrevendaTipoStatusDAO()
    return resultado.insPrevendaTipoStatus(request.json)


@app.route("/updPrevendaTipoStatus", methods=["POST"])
def updPrevendaTipoStatus():
    resultado = prevendatipostatusDAO.PrevendaTipoStatusDAO()
    return resultado.updPrevendaTipoStatus(request.json)


@app.route("/delPrevendaTipoStatus", methods=["POST"])
def delPrevendaTipoStatus():
    resultado = prevendatipostatusDAO.PrevendaTipoStatusDAO()
    return resultado.delPrevendaTipoStatus(request.json)


"""
  Fim rota: PrevendaTipoStatus
"""

"""
  Rotas do WebService para a classe: PrevendaTipoStatusVW (VW01145)
"""
import prevendatipostatusvwDAO


@app.route("/listPrevendaTipoStatusVW/", methods=["POST"])
def listPrevendaTipoStatusVW():
    resultado = prevendatipostatusvwDAO.PrevendaTipoStatusVWDAO()
    return resultado.listPrevendaTipoStatusVW(request.json)


@app.route("/dictPrevendaTipoStatusVW/", methods=["POST"])
def dictPrevendaTipoStatusVW():
    resultado = prevendatipostatusvwDAO.PrevendaTipoStatusVWDAO()
    return resultado.dictPrevendaTipoStatusVW(request.json)


@app.route("/fieldsPrevendaTipoStatusVW/", methods=["POST"])
def fieldsPrevendaTipoStatusVW():
    resultado = prevendatipostatusvwDAO.PrevendaTipoStatusVWDAO()
    return resultado.fieldsPrevendaTipoStatusVW(request.json)


@app.route("/findPrevendaTipoStatusVW/", methods=["POST"])
def findPrevendaTipoStatusVW():
    resultado = prevendatipostatusvwDAO.PrevendaTipoStatusVWDAO()
    return resultado.findPrevendaTipoStatusVW(request.json)


"""
  Fim rota: PrevendaTipoStatusVW
"""

"""
  Rotas do WebService para a classe: PrevendaHistorico (TB02306)
"""
import prevendahistoricoDAO


@app.route("/listPrevendaHistorico/", methods=["POST"])
def listPrevendaHistorico():
    resultado = prevendahistoricoDAO.PrevendaHistoricoDAO()
    return resultado.listPrevendaHistorico(request.json)


@app.route("/dictPrevendaHistorico/", methods=["POST"])
def dictPrevendaHistorico():
    resultado = prevendahistoricoDAO.PrevendaHistoricoDAO()
    return resultado.dictPrevendaHistorico(request.json)


@app.route("/fieldsPrevendaHistorico/", methods=["POST"])
def fieldsPrevendaHistorico():
    resultado = prevendahistoricoDAO.PrevendaHistoricoDAO()
    return resultado.fieldsPrevendaHistorico(request.json)


@app.route("/findPrevendaHistorico/", methods=["POST"])
def findPrevendaHistorico():
    resultado = prevendahistoricoDAO.PrevendaHistoricoDAO()
    return resultado.findPrevendaHistorico(request.json)


@app.route("/insPrevendaHistorico", methods=["POST"])
def insPrevendaHistorico():
    resultado = prevendahistoricoDAO.PrevendaHistoricoDAO()
    return resultado.insPrevendaHistorico(request.json)


@app.route("/updPrevendaHistorico", methods=["POST"])
def updPrevendaHistorico():
    resultado = prevendahistoricoDAO.PrevendaHistoricoDAO()
    return resultado.updPrevendaHistorico(request.json)


@app.route("/delPrevendaHistorico", methods=["POST"])
def delPrevendaHistorico():
    resultado = prevendahistoricoDAO.PrevendaHistoricoDAO()
    return resultado.delPrevendaHistorico(request.json)


"""
  Fim rota: PrevendaHistorico
"""

"""
  Rotas do WebService para a classe: PrevendaHistoricoVW (VW02320)
"""
import prevendahistoricovwDAO


@app.route("/listPrevendaHistoricoVW/", methods=["POST"])
def listPrevendaHistoricoVW():
    resultado = prevendahistoricovwDAO.PrevendaHistoricoVWDAO()
    return resultado.listPrevendaHistoricoVW(request.json)


@app.route("/dictPrevendaHistoricoVW/", methods=["POST"])
def dictPrevendaHistoricoVW():
    resultado = prevendahistoricovwDAO.PrevendaHistoricoVWDAO()
    return resultado.dictPrevendaHistoricoVW(request.json)


@app.route("/fieldsPrevendaHistoricoVW/", methods=["POST"])
def fieldsPrevendaHistoricoVW():
    resultado = prevendahistoricovwDAO.PrevendaHistoricoVWDAO()
    return resultado.fieldsPrevendaHistoricoVW(request.json)


@app.route("/findPrevendaHistoricoVW/", methods=["POST"])
def findPrevendaHistoricoVW():
    resultado = prevendahistoricovwDAO.PrevendaHistoricoVWDAO()
    return resultado.findPrevendaHistoricoVW(request.json)


"""
  Fim rota: PrevendaHistoricoVW
"""

"""
  Rotas do WebService para a classe: PrevendaPainelVW (VW02321)
"""
import prevendapainelvwDAO


@app.route("/listPrevendaPainelVW/", methods=["POST"])
def listPrevendaPainelVW():
    resultado = prevendapainelvwDAO.PrevendaPainelVWDAO()
    return resultado.listPrevendaPainelVW(request.json)


@app.route("/dictPrevendaPainelVW/", methods=["POST"])
def dictPrevendaPainelVW():
    resultado = prevendapainelvwDAO.PrevendaPainelVWDAO()
    return resultado.dictPrevendaPainelVW(request.json)


@app.route("/fieldsPrevendaPainelVW/", methods=["POST"])
def fieldsPrevendaPainelVW():
    resultado = prevendapainelvwDAO.PrevendaPainelVWDAO()
    return resultado.fieldsPrevendaPainelVW(request.json)


@app.route("/findPrevendaPainelVW/", methods=["POST"])
def findPrevendaPainelVW():
    resultado = prevendapainelvwDAO.PrevendaPainelVWDAO()
    return resultado.findPrevendaPainelVW(request.json)


@app.route("/delPrevendaPainelVW", methods=["POST"])
def delPrevendaPainelVW():
    resultado = prevendapainelvwDAO.PrevendaPainelVWDAO()
    return resultado.delPrevendaPainelVW(request.json)


"""
  Fim rota: PrevendaPainelVW
"""

"""
  Rotas do WebService para a classe: ProdutoPedidoVW (VW02224)
"""
import produtopedidovwDAO


@app.route("/listProdutoPedidoVW/", methods=["POST"])
def listProdutoPedidoVW():
    resultado = produtopedidovwDAO.ProdutoPedidoVWDAO()
    return resultado.listProdutoPedidoVW(request.json)


@app.route("/dictProdutoPedidoVW/", methods=["POST"])
def dictProdutoPedidoVW():
    resultado = produtopedidovwDAO.ProdutoPedidoVWDAO()
    return resultado.dictProdutoPedidoVW(request.json)


@app.route("/fieldsProdutoPedidoVW/", methods=["POST"])
def fieldsProdutoPedidoVW():
    resultado = produtopedidovwDAO.ProdutoPedidoVWDAO()
    return resultado.fieldsProdutoPedidoVW(request.json)


@app.route("/findProdutoPedidoVW/", methods=["POST"])
def findProdutoPedidoVW():
    resultado = produtopedidovwDAO.ProdutoPedidoVWDAO()
    return resultado.findProdutoPedidoVW(request.json)


"""
  Fim rota: ProdutoPedidoVW
"""

"""
  Rotas do WebService para a classe: ConsultaMovimentoVW (VW02322)
"""
import consultamovimentovwDAO


@app.route("/listConsultaMovimentoVW/", methods=["POST"])
def listConsultaMovimentoVW():
    resultado = consultamovimentovwDAO.ConsultaMovimentoVWDAO()
    return resultado.listConsultaMovimentoVW(request.json)


@app.route("/dictConsultaMovimentoVW/", methods=["POST"])
def dictConsultaMovimentoVW():
    resultado = consultamovimentovwDAO.ConsultaMovimentoVWDAO()
    return resultado.dictConsultaMovimentoVW(request.json)


@app.route("/fieldsConsultaMovimentoVW/", methods=["POST"])
def fieldsConsultaMovimentoVW():
    resultado = consultamovimentovwDAO.ConsultaMovimentoVWDAO()
    return resultado.fieldsConsultaMovimentoVW(request.json)


@app.route("/findConsultaMovimentoVW/", methods=["POST"])
def findConsultaMovimentoVW():
    resultado = consultamovimentovwDAO.ConsultaMovimentoVWDAO()
    return resultado.findConsultaMovimentoVW(request.json)


"""
  Fim rota: ConsultaMovimentoVW
"""

"""
  Rotas do WebService para a classe: ConsultaMovimentoItemVW (VW02323)
"""
import consultamovimentoitemvwDAO


@app.route("/listConsultaMovimentoItemVW/", methods=["POST"])
def listConsultaMovimentoItemVW():
    resultado = consultamovimentoitemvwDAO.ConsultaMovimentoItemVWDAO()
    return resultado.listConsultaMovimentoItemVW(request.json)


@app.route("/dictConsultaMovimentoItemVW/", methods=["POST"])
def dictConsultaMovimentoItemVW():
    resultado = consultamovimentoitemvwDAO.ConsultaMovimentoItemVWDAO()
    return resultado.dictConsultaMovimentoItemVW(request.json)


@app.route("/fieldsConsultaMovimentoItemVW/", methods=["POST"])
def fieldsConsultaMovimentoItemVW():
    resultado = consultamovimentoitemvwDAO.ConsultaMovimentoItemVWDAO()
    return resultado.fieldsConsultaMovimentoItemVW(request.json)


@app.route("/findConsultaMovimentoItemVW/", methods=["POST"])
def findConsultaMovimentoItemVW():
    resultado = consultamovimentoitemvwDAO.ConsultaMovimentoItemVWDAO()
    return resultado.findConsultaMovimentoItemVW(request.json)


"""
  Fim rota: ConsultaMovimentoItemVW
"""

"""
  Rotas do WebService para a classe: Ambiente (TB00057)
"""
import ambienteDAO


@app.route("/listAmbiente/", methods=["POST"])
def listAmbiente():
    resultado = ambienteDAO.AmbienteDAO()
    return resultado.listAmbiente(request.json)


@app.route("/dictAmbiente/", methods=["POST"])
def dictAmbiente():
    resultado = ambienteDAO.AmbienteDAO()
    return resultado.dictAmbiente(request.json)


@app.route("/fieldsAmbiente/", methods=["POST"])
def fieldsAmbiente():
    resultado = ambienteDAO.AmbienteDAO()
    return resultado.fieldsAmbiente(request.json)


@app.route("/findAmbiente/", methods=["POST"])
def findAmbiente():
    resultado = ambienteDAO.AmbienteDAO()
    return resultado.findAmbiente(request.json)


@app.route("/insAmbiente", methods=["POST"])
def insAmbiente():
    resultado = ambienteDAO.AmbienteDAO()
    return resultado.insAmbiente(request.json)


@app.route("/updAmbiente", methods=["POST"])
def updAmbiente():
    resultado = ambienteDAO.AmbienteDAO()
    return resultado.updAmbiente(request.json)


@app.route("/delAmbiente", methods=["POST"])
def delAmbiente():
    resultado = ambienteDAO.AmbienteDAO()
    return resultado.delAmbiente(request.json)


"""
  Fim rota: Ambiente
"""

"""
  Rotas do WebService para a classe: CondicaoDescontoOperacao (TB01026)
"""
import condicaodescontooperacaoDAO


@app.route("/listCondicaoDescontoOperacao/", methods=["POST"])
def listCondicaoDescontoOperacao():
    resultado = condicaodescontooperacaoDAO.CondicaoDescontoOperacaoDAO()
    return resultado.listCondicaoDescontoOperacao(request.json)


@app.route("/dictCondicaoDescontoOperacao/", methods=["POST"])
def dictCondicaoDescontoOperacao():
    resultado = condicaodescontooperacaoDAO.CondicaoDescontoOperacaoDAO()
    return resultado.dictCondicaoDescontoOperacao(request.json)


@app.route("/fieldsCondicaoDescontoOperacao/", methods=["POST"])
def fieldsCondicaoDescontoOperacao():
    resultado = condicaodescontooperacaoDAO.CondicaoDescontoOperacaoDAO()
    return resultado.fieldsCondicaoDescontoOperacao(request.json)


@app.route("/findCondicaoDescontoOperacao/", methods=["POST"])
def findCondicaoDescontoOperacao():
    resultado = condicaodescontooperacaoDAO.CondicaoDescontoOperacaoDAO()
    return resultado.findCondicaoDescontoOperacao(request.json)


@app.route("/insCondicaoDescontoOperacao", methods=["POST"])
def insCondicaoDescontoOperacao():
    resultado = condicaodescontooperacaoDAO.CondicaoDescontoOperacaoDAO()
    return resultado.insCondicaoDescontoOperacao(request.json)


@app.route("/updCondicaoDescontoOperacao", methods=["POST"])
def updCondicaoDescontoOperacao():
    resultado = condicaodescontooperacaoDAO.CondicaoDescontoOperacaoDAO()
    return resultado.updCondicaoDescontoOperacao(request.json)


@app.route("/delCondicaoDescontoOperacao", methods=["POST"])
def delCondicaoDescontoOperacao():
    resultado = condicaodescontooperacaoDAO.CondicaoDescontoOperacaoDAO()
    return resultado.delCondicaoDescontoOperacao(request.json)


"""
  Fim rota: CondicaoDescontoOperacao
"""

"""
  Rotas do WebService para a classe: CondicaoDescontoEmpresa (TB01037)
"""
import condicaodescontoempresaDAO


@app.route("/listCondicaoDescontoEmpresa/", methods=["POST"])
def listCondicaoDescontoEmpresa():
    resultado = condicaodescontoempresaDAO.CondicaoDescontoEmpresaDAO()
    return resultado.listCondicaoDescontoEmpresa(request.json)


@app.route("/dictCondicaoDescontoEmpresa/", methods=["POST"])
def dictCondicaoDescontoEmpresa():
    resultado = condicaodescontoempresaDAO.CondicaoDescontoEmpresaDAO()
    return resultado.dictCondicaoDescontoEmpresa(request.json)


@app.route("/fieldsCondicaoDescontoEmpresa/", methods=["POST"])
def fieldsCondicaoDescontoEmpresa():
    resultado = condicaodescontoempresaDAO.CondicaoDescontoEmpresaDAO()
    return resultado.fieldsCondicaoDescontoEmpresa(request.json)


@app.route("/findCondicaoDescontoEmpresa/", methods=["POST"])
def findCondicaoDescontoEmpresa():
    resultado = condicaodescontoempresaDAO.CondicaoDescontoEmpresaDAO()
    return resultado.findCondicaoDescontoEmpresa(request.json)


@app.route("/insCondicaoDescontoEmpresa", methods=["POST"])
def insCondicaoDescontoEmpresa():
    resultado = condicaodescontoempresaDAO.CondicaoDescontoEmpresaDAO()
    return resultado.insCondicaoDescontoEmpresa(request.json)


@app.route("/updCondicaoDescontoEmpresa", methods=["POST"])
def updCondicaoDescontoEmpresa():
    resultado = condicaodescontoempresaDAO.CondicaoDescontoEmpresaDAO()
    return resultado.updCondicaoDescontoEmpresa(request.json)


@app.route("/delCondicaoDescontoEmpresa", methods=["POST"])
def delCondicaoDescontoEmpresa():
    resultado = condicaodescontoempresaDAO.CondicaoDescontoEmpresaDAO()
    return resultado.delCondicaoDescontoEmpresa(request.json)


"""
  Fim rota: CondicaoDescontoEmpresa
"""

"""
  Rotas do WebService para a classe: PrevendaNotification (TB01159)
"""
import prevendanotificationDAO


@app.route("/listPrevendaNotification/", methods=["POST"])
def listPrevendaNotification():
    resultado = prevendanotificationDAO.PrevendaNotificationDAO()
    return resultado.listPrevendaNotification(request.json)


@app.route("/dictPrevendaNotification/", methods=["POST"])
def dictPrevendaNotification():
    resultado = prevendanotificationDAO.PrevendaNotificationDAO()
    return resultado.dictPrevendaNotification(request.json)


@app.route("/fieldsPrevendaNotification/", methods=["POST"])
def fieldsPrevendaNotification():
    resultado = prevendanotificationDAO.PrevendaNotificationDAO()
    return resultado.fieldsPrevendaNotification(request.json)


@app.route("/findPrevendaNotification/", methods=["POST"])
def findPrevendaNotification():
    resultado = prevendanotificationDAO.PrevendaNotificationDAO()
    return resultado.findPrevendaNotification(request.json)


@app.route("/PrevendaNotificationID", methods=["POST"])
def prevendanotificationID():
    resultado = prevendanotificationDAO.PrevendaNotificationDAO()
    return resultado.prevendanotificationID(request.json)


@app.route("/insPrevendaNotification", methods=["POST"])
def insPrevendaNotification():
    resultado = prevendanotificationDAO.PrevendaNotificationDAO()
    return resultado.insPrevendaNotification(request.json)


@app.route("/updPrevendaNotification", methods=["POST"])
def updPrevendaNotification():
    resultado = prevendanotificationDAO.PrevendaNotificationDAO()
    return resultado.updPrevendaNotification(request.json)


@app.route("/delPrevendaNotification", methods=["POST"])
def delPrevendaNotification():
    resultado = prevendanotificationDAO.PrevendaNotificationDAO()
    return resultado.delPrevendaNotification(request.json)


"""
  Fim rota: PrevendaNotification
"""

"""
  Rotas do WebService para a classe: PrevendaCustoVW (VW02324)
"""
import prevendacustovwDAO


@app.route("/listPrevendaCustoVW/", methods=["POST"])
def listPrevendaCustoVW():
    resultado = prevendacustovwDAO.PrevendaCustoVWDAO()
    return resultado.listPrevendaCustoVW(request.json)


@app.route("/dictPrevendaCustoVW/", methods=["POST"])
def dictPrevendaCustoVW():
    resultado = prevendacustovwDAO.PrevendaCustoVWDAO()
    return resultado.dictPrevendaCustoVW(request.json)


@app.route("/fieldsPrevendaCustoVW/", methods=["POST"])
def fieldsPrevendaCustoVW():
    resultado = prevendacustovwDAO.PrevendaCustoVWDAO()
    return resultado.fieldsPrevendaCustoVW(request.json)


@app.route("/findPrevendaCustoVW/", methods=["POST"])
def findPrevendaCustoVW():
    resultado = prevendacustovwDAO.PrevendaCustoVWDAO()
    return resultado.findPrevendaCustoVW(request.json)


"""
  Fim rota: PrevendaCustoVW
"""

"""
  Rotas do WebService para a classe: PedidoCompraItem (TB02031)
"""
import pedidocompraitemDAO


@app.route("/listPedidoCompraItem/", methods=["POST"])
def listPedidoCompraItem():
    resultado = pedidocompraitemDAO.PedidoCompraItemDAO()
    return resultado.listPedidoCompraItem(request.json)


@app.route("/dictPedidoCompraItem/", methods=["POST"])
def dictPedidoCompraItem():
    resultado = pedidocompraitemDAO.PedidoCompraItemDAO()
    return resultado.dictPedidoCompraItem(request.json)


@app.route("/fieldsPedidoCompraItem/", methods=["POST"])
def fieldsPedidoCompraItem():
    resultado = pedidocompraitemDAO.PedidoCompraItemDAO()
    return resultado.fieldsPedidoCompraItem(request.json)


@app.route("/findPedidoCompraItem/", methods=["POST"])
def findPedidoCompraItem():
    resultado = pedidocompraitemDAO.PedidoCompraItemDAO()
    return resultado.findPedidoCompraItem(request.json)


@app.route("/insPedidoCompraItem", methods=["POST"])
def insPedidoCompraItem():
    resultado = pedidocompraitemDAO.PedidoCompraItemDAO()
    return resultado.insPedidoCompraItem(request.json)


@app.route("/updPedidoCompraItem", methods=["POST"])
def updPedidoCompraItem():
    resultado = pedidocompraitemDAO.PedidoCompraItemDAO()
    return resultado.updPedidoCompraItem(request.json)


@app.route("/delPedidoCompraItem", methods=["POST"])
def delPedidoCompraItem():
    resultado = pedidocompraitemDAO.PedidoCompraItemDAO()
    return resultado.delPedidoCompraItem(request.json)


"""
  Fim rota: PedidoCompraItem
"""

"""
  Rotas do WebService para a classe: PrevendaParcela (TB02307)
"""
import prevendaparcelaDAO


@app.route("/listPrevendaParcela/", methods=["POST"])
def listPrevendaParcela():
    resultado = prevendaparcelaDAO.PrevendaParcelaDAO()
    return resultado.listPrevendaParcela(request.json)


@app.route("/dictPrevendaParcela/", methods=["POST"])
def dictPrevendaParcela():
    resultado = prevendaparcelaDAO.PrevendaParcelaDAO()
    return resultado.dictPrevendaParcela(request.json)


@app.route("/fieldsPrevendaParcela/", methods=["POST"])
def fieldsPrevendaParcela():
    resultado = prevendaparcelaDAO.PrevendaParcelaDAO()
    return resultado.fieldsPrevendaParcela(request.json)


@app.route("/findPrevendaParcela/", methods=["POST"])
def findPrevendaParcela():
    resultado = prevendaparcelaDAO.PrevendaParcelaDAO()
    return resultado.findPrevendaParcela(request.json)


@app.route("/insPrevendaParcela", methods=["POST"])
def insPrevendaParcela():
    resultado = prevendaparcelaDAO.PrevendaParcelaDAO()
    return resultado.insPrevendaParcela(request.json)


@app.route("/updPrevendaParcela", methods=["POST"])
def updPrevendaParcela():
    resultado = prevendaparcelaDAO.PrevendaParcelaDAO()
    return resultado.updPrevendaParcela(request.json)


@app.route("/delPrevendaParcela", methods=["POST"])
def delPrevendaParcela():
    resultado = prevendaparcelaDAO.PrevendaParcelaDAO()
    return resultado.delPrevendaParcela(request.json)


"""
  Fim rota: PrevendaParcela
"""

"""
  Rotas do WebService para a classe: Serial (TB02054)
"""
import serialDAO


@app.route("/listSerial/", methods=["POST"])
def listSerial():
    resultado = serialDAO.SerialDAO()
    return resultado.listSerial(request.json)


@app.route("/dictSerial/", methods=["POST"])
def dictSerial():
    resultado = serialDAO.SerialDAO()
    return resultado.dictSerial(request.json)


@app.route("/fieldsSerial/", methods=["POST"])
def fieldsSerial():
    resultado = serialDAO.SerialDAO()
    return resultado.fieldsSerial(request.json)


@app.route("/findSerial/", methods=["POST"])
def findSerial():
    resultado = serialDAO.SerialDAO()
    return resultado.findSerial(request.json)


@app.route("/insSerial", methods=["POST"])
def insSerial():
    resultado = serialDAO.SerialDAO()
    return resultado.insSerial(request.json)


@app.route("/updSerial", methods=["POST"])
def updSerial():
    resultado = serialDAO.SerialDAO()
    return resultado.updSerial(request.json)


@app.route("/delSerial", methods=["POST"])
def delSerial():
    resultado = serialDAO.SerialDAO()
    return resultado.delSerial(request.json)


"""
  Fim rota: Serial
"""

"""
  Rotas do WebService para a classe: SerialMov (TB02055)
"""
import serialmovDAO


@app.route("/listSerialMov/", methods=["POST"])
def listSerialMov():
    resultado = serialmovDAO.SerialMovDAO()
    return resultado.listSerialMov(request.json)


@app.route("/dictSerialMov/", methods=["POST"])
def dictSerialMov():
    resultado = serialmovDAO.SerialMovDAO()
    return resultado.dictSerialMov(request.json)


@app.route("/fieldsSerialMov/", methods=["POST"])
def fieldsSerialMov():
    resultado = serialmovDAO.SerialMovDAO()
    return resultado.fieldsSerialMov(request.json)


@app.route("/findSerialMov/", methods=["POST"])
def findSerialMov():
    resultado = serialmovDAO.SerialMovDAO()
    return resultado.findSerialMov(request.json)


@app.route("/insSerialMov", methods=["POST"])
def insSerialMov():
    resultado = serialmovDAO.SerialMovDAO()
    return resultado.insSerialMov(request.json)


@app.route("/updSerialMov", methods=["POST"])
def updSerialMov():
    resultado = serialmovDAO.SerialMovDAO()
    return resultado.updSerialMov(request.json)


@app.route("/delSerialMov", methods=["POST"])
def delSerialMov():
    resultado = serialmovDAO.SerialMovDAO()
    return resultado.delSerialMov(request.json)


"""
  Fim rota: SerialMov
"""

"""
  Rotas do WebService para a classe: ClienteEquipamento (TB01145)
"""
import clienteequipamentoDAO


@app.route("/listClienteEquipamento/", methods=["POST"])
def listClienteEquipamento():
    resultado = clienteequipamentoDAO.ClienteEquipamentoDAO()
    return resultado.listClienteEquipamento(request.json)


@app.route("/dictClienteEquipamento/", methods=["POST"])
def dictClienteEquipamento():
    resultado = clienteequipamentoDAO.ClienteEquipamentoDAO()
    return resultado.dictClienteEquipamento(request.json)


@app.route("/fieldsClienteEquipamento/", methods=["POST"])
def fieldsClienteEquipamento():
    resultado = clienteequipamentoDAO.ClienteEquipamentoDAO()
    return resultado.fieldsClienteEquipamento(request.json)


@app.route("/findClienteEquipamento/", methods=["POST"])
def findClienteEquipamento():
    resultado = clienteequipamentoDAO.ClienteEquipamentoDAO()
    return resultado.findClienteEquipamento(request.json)


@app.route("/insClienteEquipamento", methods=["POST"])
def insClienteEquipamento():
    resultado = clienteequipamentoDAO.ClienteEquipamentoDAO()
    return resultado.insClienteEquipamento(request.json)


@app.route("/updClienteEquipamento", methods=["POST"])
def updClienteEquipamento():
    resultado = clienteequipamentoDAO.ClienteEquipamentoDAO()
    return resultado.updClienteEquipamento(request.json)


@app.route("/delClienteEquipamento", methods=["POST"])
def delClienteEquipamento():
    resultado = clienteequipamentoDAO.ClienteEquipamentoDAO()
    return resultado.delClienteEquipamento(request.json)


"""
  Fim rota: ClienteEquipamento
"""

"""
  Rotas do WebService para a classe: ClienteEquipamentoVW (VW01146)
"""
import clienteequipamentovwDAO


@app.route("/listClienteEquipamentoVW/", methods=["POST"])
def listClienteEquipamentoVW():
    resultado = clienteequipamentovwDAO.ClienteEquipamentoVWDAO()
    return resultado.listClienteEquipamentoVW(request.json)


@app.route("/dictClienteEquipamentoVW/", methods=["POST"])
def dictClienteEquipamentoVW():
    resultado = clienteequipamentovwDAO.ClienteEquipamentoVWDAO()
    return resultado.dictClienteEquipamentoVW(request.json)


@app.route("/fieldsClienteEquipamentoVW/", methods=["POST"])
def fieldsClienteEquipamentoVW():
    resultado = clienteequipamentovwDAO.ClienteEquipamentoVWDAO()
    return resultado.fieldsClienteEquipamentoVW(request.json)


@app.route("/findClienteEquipamentoVW/", methods=["POST"])
def findClienteEquipamentoVW():
    resultado = clienteequipamentovwDAO.ClienteEquipamentoVWDAO()
    return resultado.findClienteEquipamentoVW(request.json)


"""
  Fim rota: ClienteEquipamentoVW
"""

"""
  Rotas do WebService para a classe: SitePermissao (TB01162)
"""
import sitepermissaoDAO


@app.route("/listSitePermissao/", methods=["POST"])
def listSitePermissao():
    resultado = sitepermissaoDAO.SitePermissaoDAO()
    return resultado.listSitePermissao(request.json)


@app.route("/dictSitePermissao/", methods=["POST"])
def dictSitePermissao():
    resultado = sitepermissaoDAO.SitePermissaoDAO()
    return resultado.dictSitePermissao(request.json)


@app.route("/fieldsSitePermissao/", methods=["POST"])
def fieldsSitePermissao():
    resultado = sitepermissaoDAO.SitePermissaoDAO()
    return resultado.fieldsSitePermissao(request.json)


@app.route("/findSitePermissao/", methods=["POST"])
def findSitePermissao():
    resultado = sitepermissaoDAO.SitePermissaoDAO()
    return resultado.findSitePermissao(request.json)


@app.route("/insSitePermissao", methods=["POST"])
def insSitePermissao():
    resultado = sitepermissaoDAO.SitePermissaoDAO()
    return resultado.insSitePermissao(request.json)


@app.route("/updSitePermissao", methods=["POST"])
def updSitePermissao():
    resultado = sitepermissaoDAO.SitePermissaoDAO()
    return resultado.updSitePermissao(request.json)


@app.route("/delSitePermissao", methods=["POST"])
def delSitePermissao():
    resultado = sitepermissaoDAO.SitePermissaoDAO()
    return resultado.delSitePermissao(request.json)


"""
  Fim rota: SitePermissao
"""

"""
  Rotas do WebService para a classe: SitePermissaoVW (VW02325)
"""
import sitepermissaovwDAO


@app.route("/listSitePermissaoVW/", methods=["POST"])
def listSitePermissaoVW():
    resultado = sitepermissaovwDAO.SitePermissaoVWDAO()
    return resultado.listSitePermissaoVW(request.json)


@app.route("/dictSitePermissaoVW/", methods=["POST"])
def dictSitePermissaoVW():
    resultado = sitepermissaovwDAO.SitePermissaoVWDAO()
    return resultado.dictSitePermissaoVW(request.json)


@app.route("/fieldsSitePermissaoVW/", methods=["POST"])
def fieldsSitePermissaoVW():
    resultado = sitepermissaovwDAO.SitePermissaoVWDAO()
    return resultado.fieldsSitePermissaoVW(request.json)


@app.route("/findSitePermissaoVW/", methods=["POST"])
def findSitePermissaoVW():
    resultado = sitepermissaovwDAO.SitePermissaoVWDAO()
    return resultado.findSitePermissaoVW(request.json)


"""
  Fim rota: SitePermissaoVW
"""

"""
  Rotas do WebService para a classe: PrecontratoDevolucao (TB02308)
"""
import precontratodevolucaoDAO


@app.route("/listPrecontratoDevolucao/", methods=["POST"])
def listPrecontratoDevolucao():
    resultado = precontratodevolucaoDAO.PrecontratoDevolucaoDAO()
    return resultado.listPrecontratoDevolucao(request.json)


@app.route("/dictPrecontratoDevolucao/", methods=["POST"])
def dictPrecontratoDevolucao():
    resultado = precontratodevolucaoDAO.PrecontratoDevolucaoDAO()
    return resultado.dictPrecontratoDevolucao(request.json)


@app.route("/fieldsPrecontratoDevolucao/", methods=["POST"])
def fieldsPrecontratoDevolucao():
    resultado = precontratodevolucaoDAO.PrecontratoDevolucaoDAO()
    return resultado.fieldsPrecontratoDevolucao(request.json)


@app.route("/findPrecontratoDevolucao/", methods=["POST"])
def findPrecontratoDevolucao():
    resultado = precontratodevolucaoDAO.PrecontratoDevolucaoDAO()
    return resultado.findPrecontratoDevolucao(request.json)


@app.route("/insPrecontratoDevolucao", methods=["POST"])
def insPrecontratoDevolucao():
    resultado = precontratodevolucaoDAO.PrecontratoDevolucaoDAO()
    return resultado.insPrecontratoDevolucao(request.json)


@app.route("/updPrecontratoDevolucao", methods=["POST"])
def updPrecontratoDevolucao():
    resultado = precontratodevolucaoDAO.PrecontratoDevolucaoDAO()
    return resultado.updPrecontratoDevolucao(request.json)


@app.route("/delPrecontratoDevolucao", methods=["POST"])
def delPrecontratoDevolucao():
    resultado = precontratodevolucaoDAO.PrecontratoDevolucaoDAO()
    return resultado.delPrecontratoDevolucao(request.json)


"""
  Fim rota: PrecontratoDevolucao
"""

"""
  Rotas do WebService para a classe: BrowseEquipVW (VW02326)
"""
import browseequipvwDAO


@app.route("/listBrowseEquipVW/", methods=["POST"])
def listBrowseEquipVW():
    resultado = browseequipvwDAO.BrowseEquipVWDAO()
    return resultado.listBrowseEquipVW(request.json)


@app.route("/dictBrowseEquipVW/", methods=["POST"])
def dictBrowseEquipVW():
    resultado = browseequipvwDAO.BrowseEquipVWDAO()
    return resultado.dictBrowseEquipVW(request.json)


@app.route("/fieldsBrowseEquipVW/", methods=["POST"])
def fieldsBrowseEquipVW():
    resultado = browseequipvwDAO.BrowseEquipVWDAO()
    return resultado.fieldsBrowseEquipVW(request.json)


@app.route("/findBrowseEquipVW/", methods=["POST"])
def findBrowseEquipVW():
    resultado = browseequipvwDAO.BrowseEquipVWDAO()
    return resultado.findBrowseEquipVW(request.json)


"""
  Fim rota: BrowseEquipVW
"""

"""
  Rotas do WebService para a classe: BrowseEquipTotalVW (VW02327)
"""
import browseequiptotalvwDAO


@app.route("/listBrowseEquipTotalVW/", methods=["POST"])
def listBrowseEquipTotalVW():
    resultado = browseequiptotalvwDAO.BrowseEquipTotalVWDAO()
    return resultado.listBrowseEquipTotalVW(request.json)


@app.route("/dictBrowseEquipTotalVW/", methods=["POST"])
def dictBrowseEquipTotalVW():
    resultado = browseequiptotalvwDAO.BrowseEquipTotalVWDAO()
    return resultado.dictBrowseEquipTotalVW(request.json)


@app.route("/fieldsBrowseEquipTotalVW/", methods=["POST"])
def fieldsBrowseEquipTotalVW():
    resultado = browseequiptotalvwDAO.BrowseEquipTotalVWDAO()
    return resultado.fieldsBrowseEquipTotalVW(request.json)


@app.route("/findBrowseEquipTotalVW/", methods=["POST"])
def findBrowseEquipTotalVW():
    resultado = browseequiptotalvwDAO.BrowseEquipTotalVWDAO()
    return resultado.findBrowseEquipTotalVW(request.json)


"""
  Fim rota: BrowseEquipTotalVW
"""

"""
  Rotas do WebService para a classe: PedidoCompraEquip (TB02208)
"""
import pedidocompraequipDAO


@app.route("/listPedidoCompraEquip/", methods=["POST"])
def listPedidoCompraEquip():
    resultado = pedidocompraequipDAO.PedidoCompraEquipDAO()
    return resultado.listPedidoCompraEquip(request.json)


@app.route("/dictPedidoCompraEquip/", methods=["POST"])
def dictPedidoCompraEquip():
    resultado = pedidocompraequipDAO.PedidoCompraEquipDAO()
    return resultado.dictPedidoCompraEquip(request.json)


@app.route("/fieldsPedidoCompraEquip/", methods=["POST"])
def fieldsPedidoCompraEquip():
    resultado = pedidocompraequipDAO.PedidoCompraEquipDAO()
    return resultado.fieldsPedidoCompraEquip(request.json)


@app.route("/findPedidoCompraEquip/", methods=["POST"])
def findPedidoCompraEquip():
    resultado = pedidocompraequipDAO.PedidoCompraEquipDAO()
    return resultado.findPedidoCompraEquip(request.json)


@app.route("/insPedidoCompraEquip", methods=["POST"])
def insPedidoCompraEquip():
    resultado = pedidocompraequipDAO.PedidoCompraEquipDAO()
    return resultado.insPedidoCompraEquip(request.json)


@app.route("/updPedidoCompraEquip", methods=["POST"])
def updPedidoCompraEquip():
    resultado = pedidocompraequipDAO.PedidoCompraEquipDAO()
    return resultado.updPedidoCompraEquip(request.json)


@app.route("/delPedidoCompraEquip", methods=["POST"])
def delPedidoCompraEquip():
    resultado = pedidocompraequipDAO.PedidoCompraEquipDAO()
    return resultado.delPedidoCompraEquip(request.json)


"""
  Fim rota: PedidoCompraEquip
"""

"""
  Rotas do WebService para a classe: PrecontratoDevolucaoVW (VW02328)
"""
import precontratodevolucaovwDAO


@app.route("/listPrecontratoDevolucaoVW/", methods=["POST"])
def listPrecontratoDevolucaoVW():
    resultado = precontratodevolucaovwDAO.PrecontratoDevolucaoVWDAO()
    return resultado.listPrecontratoDevolucaoVW(request.json)


@app.route("/dictPrecontratoDevolucaoVW/", methods=["POST"])
def dictPrecontratoDevolucaoVW():
    resultado = precontratodevolucaovwDAO.PrecontratoDevolucaoVWDAO()
    return resultado.dictPrecontratoDevolucaoVW(request.json)


@app.route("/fieldsPrecontratoDevolucaoVW/", methods=["POST"])
def fieldsPrecontratoDevolucaoVW():
    resultado = precontratodevolucaovwDAO.PrecontratoDevolucaoVWDAO()
    return resultado.fieldsPrecontratoDevolucaoVW(request.json)


@app.route("/findPrecontratoDevolucaoVW/", methods=["POST"])
def findPrecontratoDevolucaoVW():
    resultado = precontratodevolucaovwDAO.PrecontratoDevolucaoVWDAO()
    return resultado.findPrecontratoDevolucaoVW(request.json)


"""
  Fim rota: PrecontratoDevolucaoVW
"""

"""
  Rotas do WebService para a classe: Defeito (TB01048)
"""
import defeitoDAO


@app.route("/listDefeito/", methods=["POST"])
def listDefeito():
    resultado = defeitoDAO.DefeitoDAO()
    return resultado.listDefeito(request.json)


@app.route("/dictDefeito/", methods=["POST"])
def dictDefeito():
    resultado = defeitoDAO.DefeitoDAO()
    return resultado.dictDefeito(request.json)


@app.route("/fieldsDefeito/", methods=["POST"])
def fieldsDefeito():
    resultado = defeitoDAO.DefeitoDAO()
    return resultado.fieldsDefeito(request.json)


@app.route("/findDefeito/", methods=["POST"])
def findDefeito():
    resultado = defeitoDAO.DefeitoDAO()
    return resultado.findDefeito(request.json)


@app.route("/DefeitoID", methods=["POST"])
def defeitoID():
    resultado = defeitoDAO.DefeitoDAO()
    return resultado.defeitoID(request.json)


@app.route("/insDefeito", methods=["POST"])
def insDefeito():
    resultado = defeitoDAO.DefeitoDAO()
    return resultado.insDefeito(request.json)


@app.route("/updDefeito", methods=["POST"])
def updDefeito():
    resultado = defeitoDAO.DefeitoDAO()
    return resultado.updDefeito(request.json)


@app.route("/delDefeito", methods=["POST"])
def delDefeito():
    resultado = defeitoDAO.DefeitoDAO()
    return resultado.delDefeito(request.json)


"""
  Fim rota: Defeito
"""

"""
  Rotas do WebService para a classe: OsCondicaoVW (VW01106)
"""
import oscondicaovwDAO


@app.route("/listOsCondicaoVW/", methods=["POST"])
def listOsCondicaoVW():
    resultado = oscondicaovwDAO.OsCondicaoVWDAO()
    return resultado.listOsCondicaoVW(request.json)


@app.route("/dictOsCondicaoVW/", methods=["POST"])
def dictOsCondicaoVW():
    resultado = oscondicaovwDAO.OsCondicaoVWDAO()
    return resultado.dictOsCondicaoVW(request.json)


@app.route("/fieldsOsCondicaoVW/", methods=["POST"])
def fieldsOsCondicaoVW():
    resultado = oscondicaovwDAO.OsCondicaoVWDAO()
    return resultado.fieldsOsCondicaoVW(request.json)


@app.route("/findOsCondicaoVW/", methods=["POST"])
def findOsCondicaoVW():
    resultado = oscondicaovwDAO.OsCondicaoVWDAO()
    return resultado.findOsCondicaoVW(request.json)


"""
  Fim rota: OsCondicaoVW
"""

"""
  Rotas do WebService para a classe: ServicoIncompleto (TB01056)
"""
import servicoincompletoDAO


@app.route("/listServicoIncompleto/", methods=["POST"])
def listServicoIncompleto():
    resultado = servicoincompletoDAO.ServicoIncompletoDAO()
    return resultado.listServicoIncompleto(request.json)


@app.route("/dictServicoIncompleto/", methods=["POST"])
def dictServicoIncompleto():
    resultado = servicoincompletoDAO.ServicoIncompletoDAO()
    return resultado.dictServicoIncompleto(request.json)


@app.route("/fieldsServicoIncompleto/", methods=["POST"])
def fieldsServicoIncompleto():
    resultado = servicoincompletoDAO.ServicoIncompletoDAO()
    return resultado.fieldsServicoIncompleto(request.json)


@app.route("/findServicoIncompleto/", methods=["POST"])
def findServicoIncompleto():
    resultado = servicoincompletoDAO.ServicoIncompletoDAO()
    return resultado.findServicoIncompleto(request.json)


@app.route("/ServicoIncompletoID", methods=["POST"])
def servicoincompletoID():
    resultado = servicoincompletoDAO.ServicoIncompletoDAO()
    return resultado.servicoincompletoID(request.json)


@app.route("/insServicoIncompleto", methods=["POST"])
def insServicoIncompleto():
    resultado = servicoincompletoDAO.ServicoIncompletoDAO()
    return resultado.insServicoIncompleto(request.json)


@app.route("/updServicoIncompleto", methods=["POST"])
def updServicoIncompleto():
    resultado = servicoincompletoDAO.ServicoIncompletoDAO()
    return resultado.updServicoIncompleto(request.json)


@app.route("/delServicoIncompleto", methods=["POST"])
def delServicoIncompleto():
    resultado = servicoincompletoDAO.ServicoIncompletoDAO()
    return resultado.delServicoIncompleto(request.json)


"""
  Fim rota: ServicoIncompleto
"""

"""
  Rotas do WebService para a classe: TecnicoVW (VW01008)
"""
import tecnicovwDAO


@app.route("/listTecnicoVW/", methods=["POST"])
def listTecnicoVW():
    resultado = tecnicovwDAO.TecnicoVWDAO()
    return resultado.listTecnicoVW(request.json)


@app.route("/dictTecnicoVW/", methods=["POST"])
def dictTecnicoVW():
    resultado = tecnicovwDAO.TecnicoVWDAO()
    return resultado.dictTecnicoVW(request.json)


@app.route("/fieldsTecnicoVW/", methods=["POST"])
def fieldsTecnicoVW():
    resultado = tecnicovwDAO.TecnicoVWDAO()
    return resultado.fieldsTecnicoVW(request.json)


@app.route("/findTecnicoVW/", methods=["POST"])
def findTecnicoVW():
    resultado = tecnicovwDAO.TecnicoVWDAO()
    return resultado.findTecnicoVW(request.json)


"""
  Fim rota: TecnicoVW
"""

"""
  Rotas do WebService para a classe: Subgrupo (TB01018)
"""
"""
  Rotas do WebService para a classe: GrupoWebVW (VW02329)
"""
import grupowebvwDAO


@app.route("/listGrupoWebVW/", methods=["POST"])
def listGrupoWebVW():
    resultado = grupowebvwDAO.GrupoWebVWDAO()
    return resultado.listGrupoWebVW(request.json)


@app.route("/dictGrupoWebVW/", methods=["POST"])
def dictGrupoWebVW():
    resultado = grupowebvwDAO.GrupoWebVWDAO()
    return resultado.dictGrupoWebVW(request.json)


@app.route("/fieldsGrupoWebVW/", methods=["POST"])
def fieldsGrupoWebVW():
    resultado = grupowebvwDAO.GrupoWebVWDAO()
    return resultado.fieldsGrupoWebVW(request.json)


@app.route("/findGrupoWebVW/", methods=["POST"])
def findGrupoWebVW():
    resultado = grupowebvwDAO.GrupoWebVWDAO()
    return resultado.findGrupoWebVW(request.json)


"""
  Fim rota: GrupoWebVW
"""

"""
  Rotas do WebService para a classe: SubgrupoWebVW (VW02330)
"""
import subgrupowebvwDAO


@app.route("/listSubgrupoWebVW/", methods=["POST"])
def listSubgrupoWebVW():
    resultado = subgrupowebvwDAO.SubgrupoWebVWDAO()
    return resultado.listSubgrupoWebVW(request.json)


@app.route("/dictSubgrupoWebVW/", methods=["POST"])
def dictSubgrupoWebVW():
    resultado = subgrupowebvwDAO.SubgrupoWebVWDAO()
    return resultado.dictSubgrupoWebVW(request.json)


@app.route("/fieldsSubgrupoWebVW/", methods=["POST"])
def fieldsSubgrupoWebVW():
    resultado = subgrupowebvwDAO.SubgrupoWebVWDAO()
    return resultado.fieldsSubgrupoWebVW(request.json)


@app.route("/findSubgrupoWebVW/", methods=["POST"])
def findSubgrupoWebVW():
    resultado = subgrupowebvwDAO.SubgrupoWebVWDAO()
    return resultado.findSubgrupoWebVW(request.json)


"""
  Fim rota: SubgrupoWebVW
"""

"""
  Rotas do WebService para a classe: MarcaWebVW (VW02331)
"""
import marcawebvwDAO


@app.route("/listMarcaWebVW/", methods=["POST"])
def listMarcaWebVW():
    resultado = marcawebvwDAO.MarcaWebVWDAO()
    return resultado.listMarcaWebVW(request.json)


@app.route("/dictMarcaWebVW/", methods=["POST"])
def dictMarcaWebVW():
    resultado = marcawebvwDAO.MarcaWebVWDAO()
    return resultado.dictMarcaWebVW(request.json)


@app.route("/fieldsMarcaWebVW/", methods=["POST"])
def fieldsMarcaWebVW():
    resultado = marcawebvwDAO.MarcaWebVWDAO()
    return resultado.fieldsMarcaWebVW(request.json)


@app.route("/findMarcaWebVW/", methods=["POST"])
def findMarcaWebVW():
    resultado = marcawebvwDAO.MarcaWebVWDAO()
    return resultado.findMarcaWebVW(request.json)


"""
  Fim rota: MarcaWebVW
"""

"""1    
  Rotas do WebService para a classe: Subgrupo (TB01018)
"""
import subgrupoDAO


@app.route("/listSubgrupo/", methods=["POST"])
def listSubgrupo():
    resultado = subgrupoDAO.SubgrupoDAO()
    return resultado.listSubgrupo(request.json)


@app.route("/dictSubgrupo/", methods=["POST"])
def dictSubgrupo():
    resultado = subgrupoDAO.SubgrupoDAO()
    return resultado.dictSubgrupo(request.json)


@app.route("/fieldsSubgrupo/", methods=["POST"])
def fieldsSubgrupo():
    resultado = subgrupoDAO.SubgrupoDAO()
    return resultado.fieldsSubgrupo(request.json)


@app.route("/findSubgrupo/", methods=["POST"])
def findSubgrupo():
    resultado = subgrupoDAO.SubgrupoDAO()
    return resultado.findSubgrupo(request.json)


@app.route("/SubgrupoID", methods=["POST"])
def subgrupoID():
    resultado = subgrupoDAO.SubgrupoDAO()
    return resultado.subgrupoID(request.json)


@app.route("/insSubgrupo", methods=["POST"])
def insSubgrupo():
    resultado = subgrupoDAO.SubgrupoDAO()
    return resultado.insSubgrupo(request.json)


@app.route("/updSubgrupo", methods=["POST"])
def updSubgrupo():
    resultado = subgrupoDAO.SubgrupoDAO()
    return resultado.updSubgrupo(request.json)


@app.route("/delSubgrupo", methods=["POST"])
def delSubgrupo():
    resultado = subgrupoDAO.SubgrupoDAO()
    return resultado.delSubgrupo(request.json)


"""
  Fim rota: Subgrupo
"""

"""
  Rotas do WebService para a classe: StatusNotificacao (TB01059)
"""
import statusnotificacaoDAO


@app.route("/listStatusNotificacao/", methods=["POST"])
def listStatusNotificacao():
    resultado = statusnotificacaoDAO.StatusNotificacaoDAO()
    return resultado.listStatusNotificacao(request.json)


@app.route("/dictStatusNotificacao/", methods=["POST"])
def dictStatusNotificacao():
    resultado = statusnotificacaoDAO.StatusNotificacaoDAO()
    return resultado.dictStatusNotificacao(request.json)


@app.route("/fieldsStatusNotificacao/", methods=["POST"])
def fieldsStatusNotificacao():
    resultado = statusnotificacaoDAO.StatusNotificacaoDAO()
    return resultado.fieldsStatusNotificacao(request.json)


@app.route("/findStatusNotificacao/", methods=["POST"])
def findStatusNotificacao():
    resultado = statusnotificacaoDAO.StatusNotificacaoDAO()
    return resultado.findStatusNotificacao(request.json)


@app.route("/insStatusNotificacao", methods=["POST"])
def insStatusNotificacao():
    resultado = statusnotificacaoDAO.StatusNotificacaoDAO()
    return resultado.insStatusNotificacao(request.json)


@app.route("/updStatusNotificacao", methods=["POST"])
def updStatusNotificacao():
    resultado = statusnotificacaoDAO.StatusNotificacaoDAO()
    return resultado.updStatusNotificacao(request.json)


@app.route("/delStatusNotificacao", methods=["POST"])
def delStatusNotificacao():
    resultado = statusnotificacaoDAO.StatusNotificacaoDAO()
    return resultado.delStatusNotificacao(request.json)


"""
  Fim rota: StatusNotificacao
"""

"""
  Rotas do WebService para a classe: StatusWorkflow (TB01057)
"""
import statusworkflowDAO


@app.route("/listStatusWorkflow/", methods=["POST"])
def listStatusWorkflow():
    resultado = statusworkflowDAO.StatusWorkflowDAO()
    return resultado.listStatusWorkflow(request.json)


@app.route("/dictStatusWorkflow/", methods=["POST"])
def dictStatusWorkflow():
    resultado = statusworkflowDAO.StatusWorkflowDAO()
    return resultado.dictStatusWorkflow(request.json)


@app.route("/fieldsStatusWorkflow/", methods=["POST"])
def fieldsStatusWorkflow():
    resultado = statusworkflowDAO.StatusWorkflowDAO()
    return resultado.fieldsStatusWorkflow(request.json)


@app.route("/findStatusWorkflow/", methods=["POST"])
def findStatusWorkflow():
    resultado = statusworkflowDAO.StatusWorkflowDAO()
    return resultado.findStatusWorkflow(request.json)


@app.route("/insStatusWorkflow", methods=["POST"])
def insStatusWorkflow():
    resultado = statusworkflowDAO.StatusWorkflowDAO()
    return resultado.insStatusWorkflow(request.json)


@app.route("/updStatusWorkflow", methods=["POST"])
def updStatusWorkflow():
    resultado = statusworkflowDAO.StatusWorkflowDAO()
    return resultado.updStatusWorkflow(request.json)


@app.route("/delStatusWorkflow", methods=["POST"])
def delStatusWorkflow():
    resultado = statusworkflowDAO.StatusWorkflowDAO()
    return resultado.delStatusWorkflow(request.json)


"""
  Fim rota: StatusWorkflow
"""

"""
  Rotas do WebService para a classe: StatusWorkflowVW (VW01036)
"""
import statusworkflowvwDAO


@app.route("/listStatusWorkflowVW/", methods=["POST"])
def listStatusWorkflowVW():
    resultado = statusworkflowvwDAO.StatusWorkflowVWDAO()
    return resultado.listStatusWorkflowVW(request.json)


@app.route("/dictStatusWorkflowVW/", methods=["POST"])
def dictStatusWorkflowVW():
    resultado = statusworkflowvwDAO.StatusWorkflowVWDAO()
    return resultado.dictStatusWorkflowVW(request.json)


@app.route("/fieldsStatusWorkflowVW/", methods=["POST"])
def fieldsStatusWorkflowVW():
    resultado = statusworkflowvwDAO.StatusWorkflowVWDAO()
    return resultado.fieldsStatusWorkflowVW(request.json)


@app.route("/findStatusWorkflowVW/", methods=["POST"])
def findStatusWorkflowVW():
    resultado = statusworkflowvwDAO.StatusWorkflowVWDAO()
    return resultado.findStatusWorkflowVW(request.json)


"""
  Fim rota: StatusWorkflowVW
"""

"""
  Rotas do WebService para a classe: StatusUser (TB01060)
"""
import statususerDAO


@app.route("/listStatusUser/", methods=["POST"])
def listStatusUser():
    resultado = statususerDAO.StatusUserDAO()
    return resultado.listStatusUser(request.json)


@app.route("/dictStatusUser/", methods=["POST"])
def dictStatusUser():
    resultado = statususerDAO.StatusUserDAO()
    return resultado.dictStatusUser(request.json)


@app.route("/fieldsStatusUser/", methods=["POST"])
def fieldsStatusUser():
    resultado = statususerDAO.StatusUserDAO()
    return resultado.fieldsStatusUser(request.json)


@app.route("/findStatusUser/", methods=["POST"])
def findStatusUser():
    resultado = statususerDAO.StatusUserDAO()
    return resultado.findStatusUser(request.json)


@app.route("/insStatusUser", methods=["POST"])
def insStatusUser():
    resultado = statususerDAO.StatusUserDAO()
    return resultado.insStatusUser(request.json)


@app.route("/updStatusUser", methods=["POST"])
def updStatusUser():
    resultado = statususerDAO.StatusUserDAO()
    return resultado.updStatusUser(request.json)


@app.route("/delStatusUser", methods=["POST"])
def delStatusUser():
    resultado = statususerDAO.StatusUserDAO()
    return resultado.delStatusUser(request.json)


"""
  Fim rota: StatusUser
"""

"""
  Rotas do WebService para a classe: StatusWorkflowOsVW (VW01151)
"""
import statusworkflowosvwDAO


@app.route("/listStatusWorkflowOsVW/", methods=["POST"])
def listStatusWorkflowOsVW():
    resultado = statusworkflowosvwDAO.StatusWorkflowOsVWDAO()
    return resultado.listStatusWorkflowOsVW(request.json)


@app.route("/dictStatusWorkflowOsVW/", methods=["POST"])
def dictStatusWorkflowOsVW():
    resultado = statusworkflowosvwDAO.StatusWorkflowOsVWDAO()
    return resultado.dictStatusWorkflowOsVW(request.json)


@app.route("/fieldsStatusWorkflowOsVW/", methods=["POST"])
def fieldsStatusWorkflowOsVW():
    resultado = statusworkflowosvwDAO.StatusWorkflowOsVWDAO()
    return resultado.fieldsStatusWorkflowOsVW(request.json)


@app.route("/findStatusWorkflowOsVW/", methods=["POST"])
def findStatusWorkflowOsVW():
    resultado = statusworkflowosvwDAO.StatusWorkflowOsVWDAO()
    return resultado.findStatusWorkflowOsVW(request.json)


"""
  Fim rota: StatusWorkflowOsVW
"""

"""
  Rotas do WebService para a classe: MarcaCompatibilidadeVW (VW01152)
"""
import marcacompatibilidadevwDAO


@app.route("/listMarcaCompatibilidadeVW/", methods=["POST"])
def listMarcaCompatibilidadeVW():
    resultado = marcacompatibilidadevwDAO.MarcaCompatibilidadeVWDAO()
    return resultado.listMarcaCompatibilidadeVW(request.json)


@app.route("/dictMarcaCompatibilidadeVW/", methods=["POST"])
def dictMarcaCompatibilidadeVW():
    resultado = marcacompatibilidadevwDAO.MarcaCompatibilidadeVWDAO()
    return resultado.dictMarcaCompatibilidadeVW(request.json)


@app.route("/fieldsMarcaCompatibilidadeVW/", methods=["POST"])
def fieldsMarcaCompatibilidadeVW():
    resultado = marcacompatibilidadevwDAO.MarcaCompatibilidadeVWDAO()
    return resultado.fieldsMarcaCompatibilidadeVW(request.json)


@app.route("/findMarcaCompatibilidadeVW/", methods=["POST"])
def findMarcaCompatibilidadeVW():
    resultado = marcacompatibilidadevwDAO.MarcaCompatibilidadeVWDAO()
    return resultado.findMarcaCompatibilidadeVW(request.json)


"""
  Fim rota: MarcaCompatibilidadeVW
"""

"""
  Rotas do WebService para a classe: PropostaDevolucao (TB02309)
"""
import propostadevolucaoDAO


@app.route("/listPropostaDevolucao/", methods=["POST"])
def listPropostaDevolucao():
    resultado = propostadevolucaoDAO.PropostaDevolucaoDAO()
    return resultado.listPropostaDevolucao(request.json)


@app.route("/dictPropostaDevolucao/", methods=["POST"])
def dictPropostaDevolucao():
    resultado = propostadevolucaoDAO.PropostaDevolucaoDAO()
    return resultado.dictPropostaDevolucao(request.json)


@app.route("/fieldsPropostaDevolucao/", methods=["POST"])
def fieldsPropostaDevolucao():
    resultado = propostadevolucaoDAO.PropostaDevolucaoDAO()
    return resultado.fieldsPropostaDevolucao(request.json)


@app.route("/findPropostaDevolucao/", methods=["POST"])
def findPropostaDevolucao():
    resultado = propostadevolucaoDAO.PropostaDevolucaoDAO()
    return resultado.findPropostaDevolucao(request.json)


@app.route("/insPropostaDevolucao", methods=["POST"])
def insPropostaDevolucao():
    resultado = propostadevolucaoDAO.PropostaDevolucaoDAO()
    return resultado.insPropostaDevolucao(request.json)


@app.route("/updPropostaDevolucao", methods=["POST"])
def updPropostaDevolucao():
    resultado = propostadevolucaoDAO.PropostaDevolucaoDAO()
    return resultado.updPropostaDevolucao(request.json)


@app.route("/delPropostaDevolucao", methods=["POST"])
def delPropostaDevolucao():
    resultado = propostadevolucaoDAO.PropostaDevolucaoDAO()
    return resultado.delPropostaDevolucao(request.json)


"""
  Fim rota: PropostaDevolucao
"""

"""
  Rotas do WebService para a classe: BrowseEquipProVW (VW02332)
"""
import browseequipprovwDAO


@app.route("/listBrowseEquipProVW/", methods=["POST"])
def listBrowseEquipProVW():
    resultado = browseequipprovwDAO.BrowseEquipProVWDAO()
    return resultado.listBrowseEquipProVW(request.json)


@app.route("/fieldsBrowseEquipProVW/", methods=["POST"])
def fieldsBrowseEquipProVW():
    resultado = browseequipprovwDAO.BrowseEquipProVWDAO()
    return resultado.fieldsBrowseEquipProVW(request.json)


@app.route("/findBrowseEquipProVW/", methods=["POST"])
def findBrowseEquipProVW():
    resultado = browseequipprovwDAO.BrowseEquipProVWDAO()
    return resultado.findBrowseEquipProVW(request.json)


"""
  Fim rota: BrowseEquipProVW
"""

"""
  Rotas do WebService para a classe: BrowseEquipTotalProVW (VW02333)
"""
import browseequiptotalprovwDAO


@app.route("/listBrowseEquipTotalProVW/", methods=["POST"])
def listBrowseEquipTotalProVW():
    resultado = browseequiptotalprovwDAO.BrowseEquipTotalProVWDAO()
    return resultado.listBrowseEquipTotalProVW(request.json)


@app.route("/dictBrowseEquipTotalProVW/", methods=["POST"])
def dictBrowseEquipTotalProVW():
    resultado = browseequiptotalprovwDAO.BrowseEquipTotalProVWDAO()
    return resultado.dictBrowseEquipTotalProVW(request.json)


@app.route("/fieldsBrowseEquipTotalProVW/", methods=["POST"])
def fieldsBrowseEquipTotalProVW():
    resultado = browseequiptotalprovwDAO.BrowseEquipTotalProVWDAO()
    return resultado.fieldsBrowseEquipTotalProVW(request.json)


@app.route("/findBrowseEquipTotalProVW/", methods=["POST"])
def findBrowseEquipTotalProVW():
    resultado = browseequiptotalprovwDAO.BrowseEquipTotalProVWDAO()
    return resultado.findBrowseEquipTotalProVW(request.json)


"""
  Fim rota: BrowseEquipTotalProVW
"""

"""
  Rotas do WebService para a classe: ProdutoFotoVW (VW00004)
"""
import produtofotovwDAO


@app.route("/listProdutoFotoVW/", methods=["POST"])
def listProdutoFotoVW():
    resultado = produtofotovwDAO.ProdutoFotoVWDAO()
    return resultado.listProdutoFotoVW(request.json)


@app.route("/dictProdutoFotoVW/", methods=["POST"])
def dictProdutoFotoVW():
    resultado = produtofotovwDAO.ProdutoFotoVWDAO()
    return resultado.dictProdutoFotoVW(request.json)


@app.route("/fieldsProdutoFotoVW/", methods=["POST"])
def fieldsProdutoFotoVW():
    resultado = produtofotovwDAO.ProdutoFotoVWDAO()
    return resultado.fieldsProdutoFotoVW(request.json)


@app.route("/findProdutoFotoVW/", methods=["POST"])
def findProdutoFotoVW():
    resultado = produtofotovwDAO.ProdutoFotoVWDAO()
    return resultado.findProdutoFotoVW(request.json)


"""
  Fim rota: ProdutoFotoVW
"""

"""
  Rotas do WebService para a classe: ProdutoAvaliacao (TB01163)
"""
import produtoavaliacaoDAO


@app.route("/listProdutoAvaliacao/", methods=["POST"])
def listProdutoAvaliacao():
    resultado = produtoavaliacaoDAO.ProdutoAvaliacaoDAO()
    return resultado.listProdutoAvaliacao(request.json)


@app.route("/dictProdutoAvaliacao/", methods=["POST"])
def dictProdutoAvaliacao():
    resultado = produtoavaliacaoDAO.ProdutoAvaliacaoDAO()
    return resultado.dictProdutoAvaliacao(request.json)


@app.route("/fieldsProdutoAvaliacao/", methods=["POST"])
def fieldsProdutoAvaliacao():
    resultado = produtoavaliacaoDAO.ProdutoAvaliacaoDAO()
    return resultado.fieldsProdutoAvaliacao(request.json)


@app.route("/findProdutoAvaliacao/", methods=["POST"])
def findProdutoAvaliacao():
    resultado = produtoavaliacaoDAO.ProdutoAvaliacaoDAO()
    return resultado.findProdutoAvaliacao(request.json)


@app.route("/insProdutoAvaliacao", methods=["POST"])
def insProdutoAvaliacao():
    resultado = produtoavaliacaoDAO.ProdutoAvaliacaoDAO()
    return resultado.insProdutoAvaliacao(request.json)


@app.route("/updProdutoAvaliacao", methods=["POST"])
def updProdutoAvaliacao():
    resultado = produtoavaliacaoDAO.ProdutoAvaliacaoDAO()
    return resultado.updProdutoAvaliacao(request.json)


@app.route("/delProdutoAvaliacao", methods=["POST"])
def delProdutoAvaliacao():
    resultado = produtoavaliacaoDAO.ProdutoAvaliacaoDAO()
    return resultado.delProdutoAvaliacao(request.json)


"""
  Fim rota: ProdutoAvaliacao
"""


@app.route("/")
def hello_world():
    return "<p>Ola</p>"


if __name__ == "__main__":
    app.run(debug=True, port=8877)
