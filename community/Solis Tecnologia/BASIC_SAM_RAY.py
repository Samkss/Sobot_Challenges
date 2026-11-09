"""
Solis Robot - SoBot

Challenge-001-Fixed.py: Sequência sincronizada de movimentos e LEDs.
"""

from time import sleep
import serial

# Configurar a porta série
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()

# Habilita os motores das rodas
usb.write(b"MT0 E1")
sleep(0.5)

print("Iniciando percurso...")

# 1. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")
sleep(7.0) # Aguarda a conclusão do movimento

# 2. Esquerda (Azul) - Curva 90°
usb.write(b"LT E1 RD0 GR0 BL255")
usb.write(b"MT0 E1 D90 L AT3950 DT3950 V10")
sleep(5.0)

# 3. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")
sleep(7.0)

# 4. Direita (Amarelo) - Curva 90°
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(5.0)

# 5. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")
sleep(7.0)

# 6. Para trás (Vermelho) - 0.5m (-500mm)
usb.write(b"LT E1 RD255 GR0 BL0")
usb.write(b"MT0 E1 D-500 AT2500 DT2500 V10")
sleep(7.0)

# 7. Direita (Amarelo) - Curva 90°
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(5.0)

# 8. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")
sleep(7.0)

# 9. Direita (Amarelo) - Curva 90°
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(5.0)

# 10. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")
sleep(7.0)

# 11. Direita (Amarelo) - Curva 90°
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(5.0)

# Finalização: Desliga LEDs e desativa motores
usb.write(b"LT E0")
usb.write(b"MT0 E0")
print("Percurso concluído!")
