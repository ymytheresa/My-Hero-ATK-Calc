VALUES = {'ATK': 3077,  #攻強
          'ELEMENT_ATK': 958,  #屬性
          'CRIT_RATE': 421,  #暴擊值
          'CRIT_ATK': 178,  #爆傷
          'COOL_DOWN': 46, #冷卻縮減(百分比)
          'ELEMENT_MULTIPLIER': 10, #元素伤害系数(百分比)
          'SKILL_MULTIPLIER': 3.6, #技能伤害系数(百分比)
          'DMG_MULTIPLIER': 10, #伤害加成系数(百分比)
          'EXTRA_DMG_MULTIPLIER': 0, #额外伤害系数(百分比)
          'BOSS_MULTIPLIER': 54.4}  #首领伤害系数(百分比)

VALUE_CHANGES = {'ATK': 500,
                 'ELEMENT_ATK': -200,  
                 'CRIT_RATE': 0,  
                 'CRIT_ATK': 0,  
                 'COOL_DOWN': 0,
                 'ELEMENT_MULTIPLIER': 0,
                 'SKILL_MULTIPLIER': 0,
                 'DMG_MULTIPLIER': 0,
                 'EXTRA_DMG_MULTIPLIER': 0,
                 'BOSS_MULTIPLIER': 0}

def get_efficiencies(values, changes):
    atk_eff = get_atk_eff(values['ATK'])
    new_atk_eff = get_atk_eff(values['ATK'] + changes['ATK'])

    ele_eff = get_ele_eff(values['ELEMENT_ATK'], values['ELEMENT_MULTIPLIER'])
    new_ele_eff = get_ele_eff(values['ELEMENT_ATK'] + changes['ELEMENT_ATK'], values['ELEMENT_MULTIPLIER'] + changes['ELEMENT_MULTIPLIER'])

    crit_eff = get_crit_eff(values['CRIT_RATE'], values['CRIT_ATK']) 
    new_crit_eff = get_crit_eff(values['CRIT_RATE'] + changes['CRIT_RATE'], values['CRIT_ATK'] + changes['CRIT_ATK']) 

    cd_eff = get_cd_eff(values['COOL_DOWN'])
    new_cd_eff = get_cd_eff(values['COOL_DOWN'] + changes['COOL_DOWN'])

    skill_eff = get_skill_eff(values['SKILL_MULTIPLIER'])
    new_skill_eff = get_skill_eff(values['SKILL_MULTIPLIER'] + changes['SKILL_MULTIPLIER'])

    dmg_eff = get_dmg_eff(values['DMG_MULTIPLIER'])
    new_dmg_eff = get_dmg_eff(values['DMG_MULTIPLIER'] + changes['DMG_MULTIPLIER'])

    extra_dmg_eff = get_extra_dmg_eff(values['EXTRA_DMG_MULTIPLIER'])
    new_extra_dmg_eff = get_extra_dmg_eff(values['EXTRA_DMG_MULTIPLIER'] + changes['EXTRA_DMG_MULTIPLIER'])

    boss_eff = get_boss_eff(values['BOSS_MULTIPLIER'])
    new_boss_eff = get_boss_eff(values['BOSS_MULTIPLIER'] + changes['BOSS_MULTIPLIER'])

    ttl_minion_eff = get_ttl_minion_eff(atk_eff, ele_eff, crit_eff, cd_eff, skill_eff, dmg_eff, extra_dmg_eff)
    new_ttl_minion_eff = get_ttl_minion_eff(new_atk_eff, new_ele_eff, new_crit_eff, new_cd_eff, new_skill_eff, new_dmg_eff, new_extra_dmg_eff)

    ttl_boss_eff = get_ttl_boss_eff(atk_eff, ele_eff, crit_eff, cd_eff, skill_eff, dmg_eff, extra_dmg_eff, boss_eff)
    new_ttl_boss_eff = get_ttl_boss_eff(new_atk_eff, new_ele_eff, new_crit_eff, new_cd_eff, new_skill_eff, new_dmg_eff, new_extra_dmg_eff, new_boss_eff)

    eff = [ atk_eff, ele_eff, crit_eff, cd_eff, skill_eff, dmg_eff, extra_dmg_eff, boss_eff, ttl_minion_eff, ttl_boss_eff ]
    new_eff = [ new_atk_eff, new_ele_eff, new_crit_eff, new_cd_eff, new_skill_eff, new_dmg_eff, new_extra_dmg_eff, new_boss_eff, new_ttl_minion_eff, new_ttl_boss_eff ]
    
    return [eff, new_eff]

def get_atk_eff(atk):
    return atk / 700 + 1
def get_crit_eff(crit_rate, crit_atk):
    crit_rate = crit_rate if crit_rate <= 500 else 500
    if crit_rate < 200:
        final_rate = crit_rate / 400
    else:
        final_rate = crit_rate * 17 / 6000 - crit_rate * crit_rate / 60 / 10000
    return 1 - final_rate + final_rate * crit_atk
def get_ele_eff(ele_atk, ele_multi):
    return (ele_atk / 700 + 1) * (ele_multi / 100 + 1)
def get_cd_eff(cool_down):
    cool_down = cool_down if cool_down <= 45 else 45
    return 100 / (100 - cool_down)
def get_skill_eff(skill_multi):
    return skill_multi / 100 + 1
def get_dmg_eff(dmg_multi):
    return dmg_multi / 100 + 1
def get_extra_dmg_eff(extra_dmg_multi):
    return extra_dmg_multi / 100 + 1
def get_boss_eff(boss_atk):
    return boss_atk / 100 + 1
def get_minion_atk_eff():
    return 1
def get_ttl_minion_eff(atk_eff, ele_eff, crit_eff, cd_eff, skill_eff, dmg_eff, extra_dmg_eff):
    return atk_eff * ele_eff * crit_eff * cd_eff * skill_eff * dmg_eff * extra_dmg_eff
def get_ttl_boss_eff(atk_eff, ele_eff, crit_eff, cd_eff, skill_eff, dmg_eff, extra_dmg_eff, boss_eff):
    return atk_eff * ele_eff * crit_eff * cd_eff * skill_eff * dmg_eff * extra_dmg_eff * boss_eff

all_efficiencies = get_efficiencies(VALUES, VALUE_CHANGES)
efficiencies = all_efficiencies[0]
new_efficiencies = all_efficiencies[1]

description_list = [
    '攻強效益', '屬性效益',  '暴擊效益', '冷卻效益', '技傷加成', '傷害加成', '額外傷害加成', '首領效益', '小怪總效益', '首領總效益'
]

for i in range(len(description_list)):
    e = efficiencies[i] * 100
    new_e = new_efficiencies[i] * 100
    change = (new_e - e) / e * 100
    header = description_list[i]
    for i in range(6 - len(header)):
        header += '  '
    header += ' '
    print('%s:   %s   > %s    |>   改變 : %s' %(header, '{:>12}'.format(f'{e:.2f}%'), '{:>12}'.format(f'{new_e:.2f}%'), '{:>12}'.format(f'{change:.2f}%')))
