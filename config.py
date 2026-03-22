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
        "description": "Investigue como temperatura, umidade e ventilação interagem para definir o conforto térmico em ambientes reais. Analise dados ambientais e compreenda, na prática, os mecanismos de transferência de calor que afetam o bem-estar das pessoas."
    },
    {
        "app_id": "app_02",
        "title": "Sistemas de Bombeamento de Água",
        "subtitle": "Eletricidade Aplicada",
        "card_image": "ba001.png",
        "description": "Explore como motores elétricos, sensores e painéis de controle operam juntos para movimentar água em edifícios e instalações industriais. Entenda o funcionamento dos sistemas de acionamento e controle utilizados no bombeamento moderno."
    },
    {
        "app_id": "app_03",
        "title": "Dinâmica do Bombeamento de Água",
        "subtitle": "Mecânica dos Fluidos Aplicada",
        "card_image": "ba002.png",
        "description": "Analise pressão, vazão e perdas de carga em sistemas de tubulação. Descubra como os princípios da mecânica dos fluidos explicam o comportamento da água em redes de bombeamento reais."
    },
    {
        "app_id": "app_04",
        "title": "Sistema de Produção de Frangos de Postura",
        "subtitle": "Monitoramento Inteligente do Aviário",
        "card_image": "av001.png",
        "description": "Explore como sensores, ventilação e controle ambiental são utilizados para monitorar o ambiente do aviário. Investigue como dados e automação contribuem para o bem-estar das aves e a eficiência da produção."
    },
    {
        "app_id": "app_05",
        "title": "Backup de Energia em Circuitos Eletrônicos",
        "subtitle": "Energia de Reserva na Prática",
        "card_image": "el001.png",
        "description": "Investigue como sistemas eletrônicos garantem continuidade de energia quando ocorre falha na alimentação principal. Explore o funcionamento de sensores, microcontroladores e circuitos de reserva utilizados em dispositivos baseados em ESP32."
    }
    {
        "app_id": "app_12",
        "title": "Sistemas de Bombeamento de Água",
        "subtitle": "Soluções em Dimensionamento de Fios",
        "card_image": "ba001.png",
        "description": "Explore como motores elétricos, sensores e painéis de controle operam juntos para movimentar água em edifícios e instalações industriais. Entenda o funcionamento dos sistemas de acionamento e controle utilizados no bombeamento moderno."
    },
    
]


