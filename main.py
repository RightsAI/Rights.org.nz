# RIGHTS.ORG.NZ — Main System Launcher

from core.boot import boot_system

if __name__ == "__main__":
    print("=== RIGHTS.ORG.NZ SYSTEM START ===")
    status = boot_system()
    print(status)
    print("=== SYSTEM READY ===")
