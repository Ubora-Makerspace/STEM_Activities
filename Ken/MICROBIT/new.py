import machine
import time
import gc

# Configure the internal temperature sensor (ADC channel 4 on RP2040)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535

print("=== Raspberry Pi Pico Internal Hardware Test ===")
print(f"CPU Frequency: {machine.freq() / 1_000_000:.1f} MHz")

# Collect memory stats
gc.collect()
free_ram = gc.mem_free()
allocated_ram = gc.mem_alloc()
print(f"Free RAM: {free_ram / 1024:.2f} KB | Used RAM: {allocated_ram / 1024:.2f} KB")
print("-------------------------------------------------")
led = machine.Pin("LED", machine.Pin.OUT)
try:
    while True:
        # Read the raw 16-bit analog value from the internal thermal diode
        led.toggle()
        reading = sensor_temp.read_u16() * conversion_factor

        # Standard RP2040 formula: T = 27 - (V - 0.706) / 0.001721
        temperature_c = 27 - (reading - 0.706) / 0.001721
        temperature_f = temperature_c * (9 / 5) + 32

        # Print current runtime status
        uptime_s = time.ticks_ms() // 1000
        print(f"[{uptime_s:04d}s] Core Temp: {temperature_c:.2f} °C ({temperature_f:.2f} °F) | Voltage: {reading:.3f} V")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nSelf-test finished.")
