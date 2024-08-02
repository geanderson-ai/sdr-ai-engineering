
import numpy_financial as npf



def calcular_roi(valor_inicial, valor_final):
    """
    Calcula o Retorno sobre o Investimento (ROI).

    :param valor_inicial: O valor inicial investido.
    :param valor_final: O valor final obtido após o investimento.
    :return: O ROI como uma porcentagem.
    """
    try:
        # Calcula o ROI
        roi = ((valor_final - valor_inicial) / valor_inicial) * 100
        return roi
    except ZeroDivisionError:
        return "O valor inicial não pode ser zero."



def calcular_vpl(fluxos_caixa, taxa_desconto, investimento_inicial):
    """
    Calcula o Valor Presente Líquido (VPL).

    :param fluxos_caixa: Lista de fluxos de caixa futuros.
    :param taxa_desconto: Taxa de desconto.
    :param investimento_inicial: Investimento inicial.
    :return: O VPL.
    """
    vpl = -investimento_inicial
    for t, fluxo in enumerate(fluxos_caixa):
        vpl += fluxo / (1 + taxa_desconto) ** (t + 1)
    return vpl

def calcular_tir(fluxos_caixa):
    """
    Calcula a Taxa Interna de Retorno (TIR).

    :param fluxos_caixa: Lista de fluxos de caixa, incluindo investimento inicial negativo.
    :return: A TIR como uma porcentagem.
    """
    tir = npf.irr(fluxos_caixa)
    return tir

def calcular_payback(fluxos_caixa):
    """
    Calcula o período de retorno (Payback).

    :param fluxos_caixa: Lista de fluxos de caixa, incluindo investimento inicial negativo.
    :return: O período de retorno em anos.
    """
    acumulado = 0
    for t, fluxo in enumerate(fluxos_caixa):
        acumulado += fluxo
        if acumulado >= 0:
            return t + 1
    return None  # Não recupera o investimento

def calcular_tco(custos_iniciais, custos_manutencao, anos):
    """
    Calcula o Custo Total de Propriedade (TCO).

    :param custos_iniciais: Custo inicial do projeto.
    :param custos_manutencao: Custos de manutenção anuais.
    :param anos: Número de anos do projeto.
    :return: O custo total de propriedade.
    """
    tco = custos_iniciais + (custos_manutencao * anos)
    return tco

def calcular_bcr(beneficios_totais, custos_totais):
    """
    Calcula a razão benefício-custo (BCR).

    :param beneficios_totais: Valor total dos benefícios esperados.
    :param custos_totais: Custo total do projeto.
    :return: A razão benefício-custo.
    """
    bcr = beneficios_totais / custos_totais
    return bcr

# Exemplo de uso das funções

if __name__ == "__main__":
    # Exemplo de ROI
    valor_inicial = 1000
    valor_final = 1200
    roi = calcular_roi(valor_inicial, valor_final)
    print(f"O ROI é {roi:.2f}%")

    # Exemplo de VPL
    fluxos_caixa = [3000, 4000, 5000]  # Fluxos de caixa esperados nos próximos anos
    taxa_desconto = 0.1  # 10%
    investimento_inicial = 7000
    vpl = calcular_vpl(fluxos_caixa, taxa_desconto, investimento_inicial)
    print(f"O VPL é {vpl:.2f}")

    # Exemplo de TIR
    fluxos_caixa_tir = [-7000, 3000, 4000, 5000]  # Inclui investimento inicial negativo
    tir = calcular_tir(fluxos_caixa_tir)
    print(f"A TIR é {tir:.2%}")

    # Exemplo de Payback
    fluxos_caixa_payback = [-7000, 3000, 4000, 5000]
    payback = calcular_payback(fluxos_caixa_payback)
    print(f"O período de retorno é {payback} anos")

    # Exemplo de TCO
    custos_iniciais = 10000
    custos_manutencao = 2000
    anos = 3
    tco = calcular_tco(custos_iniciais, custos_manutencao, anos)
    print(f"O custo total de propriedade é {tco:.2f}")

    # Exemplo de BCR
    beneficios_totais = 15000
    custos_totais = 10000
    bcr = calcular_bcr(beneficios_totais, custos_totais)
    print(f"A razão benefício-custo é {bcr:.2f}")
