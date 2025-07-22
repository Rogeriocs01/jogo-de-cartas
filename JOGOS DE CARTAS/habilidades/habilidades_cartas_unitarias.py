from habilidades import habilidades_utils as utils

def executar(carta_id, jogador, inimigo, campo):
    funcoes = {
        'Carta_1': carta_1,
        'Carta_2': carta_2,
        'Carta_3': carta_3,
        'Carta_4': carta_4,
        'Carta_5': carta_5,
        'Carta_6': carta_6,
        'Carta_7': carta_7,
        'Carta_8': carta_8,
        'Carta_9': carta_9,
        'Carta_10': carta_10,
        'Carta_11': carta_11,
        'Carta_12': carta_12,
        'Carta_13': carta_13,
        'Carta_14': carta_14,
        'Carta_15': carta_15,
        'Carta_16': carta_16,
        'Carta_17': carta_17,
        'Carta_18': carta_18,
        'Carta_19': carta_19,
        'Carta_20': carta_20,
        'Carta_21': carta_21,
        'Carta_22': carta_22,
        'Carta_23': carta_23,
        'Carta_24': carta_24,
        'Carta_25': carta_25,
        'Carta_26': carta_26,
        'Carta_27': carta_27,
        'Carta_28': carta_28,
        'Carta_29': carta_29,
        'Carta_30': carta_30,
        'Carta_31': carta_31,
        'Carta_32': carta_32,
        'Carta_33': carta_33,
        'Carta_34': carta_34,
        'Carta_35': carta_35,
        'Carta_36': carta_36,
        'Carta_37': carta_37,
        'Carta_38': carta_38,
        'Carta_39': carta_39,
        'Carta_40': carta_40,
        'Carta_41': carta_41,
        'Carta_42': carta_42,
        'Carta_43': carta_43,
        'Carta_44': carta_44,
        'Carta_45': carta_45,
        'Carta_46': carta_46,
        'Carta_47': carta_47,
        'Carta_48': carta_48,
        'Carta_49': carta_49,
        'Carta_50': carta_50,
        'Carta_51': carta_51,
        'Carta_52': carta_52,
        'Carta_53': carta_53,
        'Carta_54': carta_54,
        'Carta_55': carta_55,
        'Carta_56': carta_56,
        'Carta_57': carta_57,
        'Carta_58': carta_58,
        'Carta_59': carta_59,
        'Carta_60': carta_60,
        'Carta_61': carta_61,
        'Carta_62': carta_62,
        'Carta_63': carta_63,
        'Carta_64': carta_64,
        'Carta_65': carta_65,
        'Carta_66': carta_66,
        'Carta_67': carta_67,
        'Carta_68': carta_68,
        'Carta_69': carta_69,
        'Carta_70': carta_70,
        'Carta_71': carta_71,
        'Carta_72': carta_72,
        'Carta_73': carta_73,
        'Carta_74': carta_74,
        'Carta_75': carta_75,
        'Carta_76': carta_76,
        'Carta_77': carta_77,
        'Carta_78': carta_78,
        'Carta_79': carta_79,
        'Carta_80': carta_80,
    }

def carta_1(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 3)

def carta_2(jogador, inimigo, campo):
    utils.curar(jogador, 1)

def carta_3(jogador, inimigo, campo):
    if jogador.campo:
        utils.buff_defesa(jogador.campo[0], 2)

def carta_4(jogador, inimigo, campo):
    for carta in jogador.campo:
        utils.buff_ataque(carta, 1)
        utils.buff_defesa(carta, 1)

def carta_5(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 2)

def carta_6(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 2)

def carta_7(jogador, inimigo, campo):
    utils.curar(jogador, 2)

def carta_8(jogador, inimigo, campo):
    utils.buff_ataque_todos(jogador.campo, 1)

def carta_9(jogador, inimigo, campo):
    if jogador.campo:
        utils.buff_ataque(jogador.campo[0], 2)

def carta_10(jogador, inimigo, campo):
    utils.curar(jogador, 3)

def carta_11(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 1)

def carta_12(jogador, inimigo, campo):
    utils.curar(jogador, 2)

def carta_13(jogador, inimigo, campo):
    if jogador.campo:
        utils.buff_defesa(jogador.campo[0], 3)

def carta_14(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 1)

def carta_15(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 2)

def carta_16(jogador, inimigo, campo):
    for carta in jogador.campo:
        utils.buff_defesa(carta, 2)

def carta_17(jogador, inimigo, campo):
    if jogador.campo:
        utils.buff_ataque(jogador.campo[0], 1)

def carta_18(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 3)

def carta_19(jogador, inimigo, campo):
    utils.buff_ataque_todos(jogador.campo, 1)

def carta_20(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 2)


def carta_21(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 3)

def carta_22(jogador, inimigo, campo):
    utils.curar(jogador, 3)

def carta_23(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 4)

def carta_24(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_25(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 2)

def carta_26(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 3)

def carta_27(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_28(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 3)

def carta_29(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_30(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 2)

def carta_31(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_32(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 5)

def carta_33(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 4)

def carta_34(jogador, inimigo, campo):
    utils.curar(jogador, 2)

def carta_35(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_36(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 2)

def carta_37(jogador, inimigo, campo):
    utils.curar(jogador, 2)

def carta_38(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 3)

def carta_39(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_40(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 3)

def carta_41(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 3)

def carta_42(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 3)

def carta_43(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_44(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_45(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 4)

def carta_46(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_47(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 2)

def carta_48(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 4)

def carta_49(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 3)

def carta_50(jogador, inimigo, campo):
    for carta in jogador.campo:
        utils.buff_defesa(carta, 2)

def carta_51(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 5)

def carta_52(jogador, inimigo, campo):
    utils.curar(jogador, 3)

def carta_53(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 4)

def carta_54(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_55(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 3)

def carta_56(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_57(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 4)

def carta_58(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_59(jogador, inimigo, campo):
    for carta in jogador.campo:
        utils.buff_defesa(carta, 2)

def carta_60(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_61(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 3)

def carta_62(jogador, inimigo, campo):
    utils.curar(jogador, 4)

def carta_63(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_64(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 3)

def carta_65(jogador, inimigo, campo):
    utils.curar(jogador, 2)

def carta_66(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_67(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 3)

def carta_68(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 4)

def carta_69(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_70(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 2)

def carta_71(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_72(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_73(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 4)

def carta_74(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 1)

def carta_75(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 2)

def carta_76(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_77(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 3)

def carta_78(jogador, inimigo, campo):
    utils.buff_ataque(jogador, 2)

def carta_79(jogador, inimigo, campo):
    utils.buff_defesa(jogador, 4)

def carta_80(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 4)