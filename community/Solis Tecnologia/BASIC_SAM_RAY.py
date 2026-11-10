"""
Solis Robot - SoBot

Challenge-001-Basic.py: Rota exata com esfera de aço e sinalização LED.
Company: Solis Tecnologia
"""

from time import sleep
import serial

# Configurar a porta série
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()     # Aguarda configuração da comunicação

# Habilita os motores das rodas
usb.write(b"MT0 E1")
sleep(0.5)

print("Iniciando percurso com a nova roda esférica...")

# -------------------------------------------------------------
# IDA (Setas Azuis)
# -------------------------------------------------------------

# 1. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 2. Esquerda (Azul) - Curva 90° sobre o próprio eixo
usb.write(b"LT E1 RD0 GR0 BL255")
usb.write(b"MT0 E1 D90 L AT1000 DT1000 V10")
sleep(4.0)

# 3. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 4. Direita (Amarelo) - Curva 90° sobre o próprio eixo
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT1000 DT1000 V10")
sleep(4.0)

# 5. Para frente (Verde) - 0.5m (Chega até a barra de parada)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# -------------------------------------------------------------
# RETORNO NA BARRA (Setas Lilás)
# -------------------------------------------------------------

# Giro 180° na Barra (Vermelho) - Retorno de frente
usb.write(b"LT E1 RD255 GR0 BL0")
usb.write(b"MT0 E1 D180 R AT1000 DT1000 V10")
sleep(5.0)

# 6. Para frente (Verde) - 0.5m
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 7. Direita (Amarelo) - Curva 90° sobre o próprio eixo
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT1000 DT1000 V10")
sleep(4.0)

# 8. Para frente (Verde) - 0.5m
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 9. Direita (Amarelo) - Curva 90° sobre o próprio eixo
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT1000 DT1000 V10")
sleep(4.0)

# 10. Para frente (Verde) - 0.5m
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 11. Direita / Retorno ao ponto inicial (Amarelo)
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D180 R AT1000 DT1000 V10")
sleep(5.0)

# Finalização
usb.write(b"LT E0")
usb.write(b"MT0 E0")
print("Percurso concluído com sucesso!")
