import os
import re
import sys

def apply_rebranding(base_dir):
    print(f"Applying HexDesk rebranding patches from base directory: {base_dir}")
    
    # 1. libs/hbb_common/src/config.rs
    config_path = os.path.join(base_dir, "libs", "hbb_common", "src", "config.rs")
    if os.path.exists(config_path):
        print(f"Patching config.rs at {config_path}...")
        with open(config_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        patched = content
        patched = patched.replace('RwLock::new("RustDesk".to_owned())', 'RwLock::new("HexDesk".to_owned())')
        patched = patched.replace("rs-ny.rustdesk.com", "hexdesk.com.tr")
        patched = patched.replace("OeVuKk5nlHiXp+APNn0Y3pC1Iwpwn44JGqrQCsWqmBw=", "uCzBnD5VRqcscpc0HOvxnjOakhoedBZqid+EsGJ4byQ=")
        patched = patched.replace("https://rustdesk.com/docs/en/", "https://hexdesk.com.tr")
        patched = patched.replace("https://rustdesk.com/docs/en/manual/linux/#x11-required", "https://hexdesk.com.trmanual/linux/#x11-required")
        
        if patched != content:
            with open(config_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print("config.rs patched successfully!")
        else:
            print("config.rs no changes.")

    # 2. src/common.rs
    common_path = os.path.join(base_dir, "src", "common.rs")
    if os.path.exists(common_path):
        print(f"Patching {common_path}...")
        with open(common_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        patched = content
        target_fn = """pub fn using_public_server() -> bool {
    crate::get_custom_rendezvous_server(get_option("custom-rendezvous-server")).is_empty()
}"""
        replacement_fn = """pub fn using_public_server() -> bool {
    false
}"""
        patched = patched.replace(target_fn, replacement_fn)
        if replacement_fn not in patched:
            patched = re.sub(r'pub fn using_public_server\(\) -> bool \{\s+crate::get_custom_rendezvous_server\(get_option\("custom-rendezvous-server"\)\)\.is_empty\(\)\s+\}', 'pub fn using_public_server() -> bool {\n    false\n}', patched)
            
        # Also replace admin.rustdesk.com with hexdesk.com.tr
        patched = patched.replace('"https://admin.rustdesk.com"', '"https://hexdesk.com.tr"')
            
        if patched != content:
            with open(common_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print("common.rs patched successfully!")
        else:
            print("common.rs no changes.")

    # 3. src/main.rs
    main_path = os.path.join(base_dir, "src", "main.rs")
    if os.path.exists(main_path):
        print(f"Patching {main_path}...")
        with open(main_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        patched = content
        patched = patched.replace('.author("Purslane Ltd<info@rustdesk.com>")', '.author("Hex Yazılım<info@hexdesk.com.tr>")')
        
        if patched != content:
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print("main.rs patched successfully!")
        else:
            print("main.rs no changes.")

    # 4. flutter/lib/desktop/pages/desktop_setting_page.dart
    setting_path = os.path.join(base_dir, "flutter", "lib", "desktop", "pages", "desktop_setting_page.dart")
    if os.path.exists(setting_path):
        print(f"Patching {setting_path}...")
        with open(setting_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        patched = content
        patched = patched.replace("Purslane Ltd.", "Hex Yazılım")
        
        if patched != content:
            with open(setting_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print("desktop_setting_page.dart patched successfully!")
        else:
            print("desktop_setting_page.dart no changes.")

    # 5. src/ui/index.tis
    tis_path = os.path.join(base_dir, "src", "ui", "index.tis")
    if os.path.exists(tis_path):
        print(f"Patching {tis_path}...")
        with open(tis_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        patched = content
        patched = patched.replace("Purslane Ltd.", "Hex Yazılım")
        patched = patched.replace("https://rustdesk.com/privacy.html", "https://hexdesk.com.tr/privacy")
        patched = patched.replace("https://rustdesk.com", "https://hexdesk.com.tr")
        
        if patched != content:
            with open(tis_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print("index.tis patched successfully!")
        else:
            print("index.tis no changes.")

    # 6. Cargo.toml
    cargo_path = os.path.join(base_dir, "Cargo.toml")
    if os.path.exists(cargo_path):
        print(f"Patching {cargo_path}...")
        with open(cargo_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        patched = content
        patched = patched.replace('LegalCopyright = "Copyright © 2025 Purslane Ltd. All rights reserved."', 'LegalCopyright = "Copyright © 2026 Hex Yazılım. Tüm hakları saklıdır."')
        patched = patched.replace('ProductName = "RustDesk"', 'ProductName = "HexDesk"')
        patched = patched.replace('FileDescription = "RustDesk Remote Desktop"', 'FileDescription = "HexDesk Uzaktan Erişim Programı"')
        patched = patched.replace('OriginalFilename = "rustdesk.exe"', 'OriginalFilename = "HexDesk.exe"')
        
        if patched != content:
            with open(cargo_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print("Cargo.toml patched successfully!")
        else:
            print("Cargo.toml no changes.")

    # 7. libs/portable/Cargo.toml
    portable_cargo_path = os.path.join(base_dir, "libs", "portable", "Cargo.toml")
    if os.path.exists(portable_cargo_path):
        print(f"Patching {portable_cargo_path}...")
        with open(portable_cargo_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        patched = content
        patched = patched.replace('LegalCopyright = "Copyright © 2025 Purslane Ltd. All rights reserved."', 'LegalCopyright = "Copyright © 2026 Hex Yazılım. Tüm hakları saklıdır."')
        patched = patched.replace('ProductName = "RustDesk"', 'ProductName = "HexDesk"')
        patched = patched.replace('FileDescription = "RustDesk Remote Desktop"', 'FileDescription = "HexDesk Uzaktan Erişim Programı"')
        patched = patched.replace('OriginalFilename = "rustdesk.exe"', 'OriginalFilename = "HexDesk.exe"')
        
        if patched != content:
            with open(portable_cargo_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print("libs/portable/Cargo.toml patched successfully!")
        else:
            print("libs/portable/Cargo.toml no changes.")

if __name__ == "__main__":
    apply_rebranding(".")
