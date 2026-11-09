"""
Solis Robot - SoBot

Challenge-001-Basic.py: Sequence of movements using fixed commands and LED signaling.

Company: Solis Tecnologia
"""

from time import sleep
import serial

# Set serial port
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()     # Waits data configuration

# Enables wheel motors
usb.write(b"MT0 E1")
sleep(0.1)

# 1. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")

# 2. Esquerda (Azul)
usb.write(b"LT E1 RD0 GR0 BL255")
usb.write(b"MT0 E1 D90 L AT3950 DT3950 V10")

# 3. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")

# 4. Direita (Amarelo)
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")

# 5. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")

# 6. Para trás (Vermelho) - 1.0m (1000mm)
usb.write(b"LT E1 RD255 GR0 BL0")
usb.write(b"MT0 E1 D-1000 AT5000 DT5000 V10")

# 7. Direita (Amarelo)
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")

# 8. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")

# 9. Direita (Amarelo)
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")

# 10. Para frente (Verde) - 0.5m (500mm)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT2500 DT2500 V10")

# 11. Direita (Amarelo)
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")

# Turn off led tape and disable wheel motors
usb.write(b"LT E1 RD0 GR0 BL0")
usb.write(b"MT0 E0")