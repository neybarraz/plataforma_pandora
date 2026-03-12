# config.py

import os

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "neybarraz")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
DATABASE_PATH = os.getenv("DATABASE_PATH", "database/db.sqlite")


APP_CATALOG = [
    {
        "app_id": "app_01",
        "title": "Conforto Térmico em Ambientes",
        "subtitle": "Termodinâmica Aplicada",
        "card_image": "ct001.png",
        "description": "Investigue como temperatura, umidade e ventilação influenciam o conforto térmico das pessoas e aprenda a interpretar fenômenos de transferência de calor em ambientes reais."
    },
    {
        "app_id": "app_02",
        "title": "Sistemas de Bombeamento de Água",
        "subtitle": "Eletricidade Aplicada I",
        "card_image": "ba001.png",
        "description": "Explore como motores elétricos, sensores e painéis de controle trabalham juntos para movimentar água em edifícios e sistemas industriais modernos."
    },
    {
        "app_id": "app_03",
        "title": "Dinâmica do Bombeamento de Água",
        "subtitle": "Mecânica dos Fluidos",
        "card_image": "ba002.png",
        "description": "Analise pressão, vazão e perdas de carga em tubulações e descubra os princípios físicos que governam o transporte de fluidos."
    },
    {
        "app_id": "app_04",
        "title": "Produção Intensiva de Frangos de Postura",
        "subtitle": "Monitoramento Inteligente do Aviário",
        "card_image": "av001.png",
        "description": "Descubra como sensores, ventilação e controle ambiental são utilizados para monitorar o bem-estar das aves e otimizar a produção em sistemas modernos de postura."
    },
    {
        "app_id": "app_05",
        "title": "Como Funciona o Backup de Energia em Circuitos Eletrônicos?",
        "subtitle": "Energia de Reserva na Prática",
        "card_image": "el001.png",
        "description": "Explore como sensores, eletrônica e sistemas de energia trabalham juntos para medir temperatura, umidade e iluminação em tempo real. Descubra como um dispositivo baseado em ESP32 transforma fenômenos físicos em dados que revelam o funcionamento do ambiente."
    }

]

