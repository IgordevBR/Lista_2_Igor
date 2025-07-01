import time # importa a biblioteca time para simular o tempo de espera
from datetime import datetime, timedelta # importa datetime e timedelta para manipulação de datas e horas

def lembrete_agua():
    print("=== Sistema de Lembrete para Beber Água ===")

    try:
        # Entrada de horários
        hora_inicio = int(input("Digite a hora de início (0-23): "))
        hora_fim = int(input("Digite a hora de término (0-23): "))
        intervalo = int(input("Digite o intervalo entre os lembretes (em minutos): "))

        # Validação dos dados
        if not (0 <= hora_inicio < 24) or not (0 < hora_fim <= 24):
            print("❌ Horário inválido. Use valores entre 0 e 23.")
            return
        if hora_inicio >= hora_fim:
            print("❌ Hora de início deve ser menor que a hora de término.")
            return
        if intervalo <= 0:
            print("❌ Intervalo deve ser maior que zero.")
            return

        # Definir o horário atual do sistema
        agora = datetime.now()
        hora_atual = agora.replace(hour=hora_inicio, minute=0, second=0, microsecond=0)

        fim_do_dia = agora.replace(hour=hora_fim, minute=0, second=0, microsecond=0)

        print(f"\n⏰ Lembretes iniciados das {hora_inicio}:00 até às {hora_fim}:00, a cada {intervalo} minutos.\n")

        # Loop dos lembretes
        while hora_atual <= fim_do_dia:
            print(f"[{hora_atual.strftime('%H:%M')}] 💧 Hora de beber água!")
            hora_atual += timedelta(minutes=intervalo)
            time.sleep(1)  # Simula o tempo de espera

        print("\n✅ Fim dos lembretes de hoje. Parabéns por se hidratar!")

    except ValueError:
        print("❌ Erro: Digite apenas números inteiros válidos.")

# Chamar a função
lembrete_agua()
