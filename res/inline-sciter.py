import re
import os
import sys

# Patch codebase dynamically with company values
try:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
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
        if patched != content:
            with open(common_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print("common.rs patched successfully!")

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

except Exception as e:
    print(f"Failed to apply rebranding patches: {e}")


def strip(s): return re.sub(r'\s+\n', '\n', re.sub(r'\n\s+', '\n', s))

common_css = open('src/ui/common.css').read()
common_tis = open('src/ui/common.tis', encoding='UTF8').read()

index = open('src/ui/index.html').read() \
    .replace('@import url(index.css);', open('src/ui/index.css').read()) \
    .replace('include "index.tis";', open('src/ui/index.tis').read()) \
    .replace('include "msgbox.tis";', open('src/ui/msgbox.tis').read()) \
    .replace('include "ab.tis";', open('src/ui/ab.tis').read())

remote = open('src/ui/remote.html').read() \
    .replace('@import url(remote.css);', open('src/ui/remote.css').read()) \
    .replace('@import url(header.css);', open('src/ui/header.css').read()) \
    .replace('@import url(file_transfer.css);', open('src/ui/file_transfer.css').read()) \
    .replace('include "remote.tis";', open('src/ui/remote.tis').read()) \
    .replace('include "msgbox.tis";', open('src/ui/msgbox.tis').read()) \
    .replace('include "grid.tis";', open('src/ui/grid.tis').read()) \
    .replace('include "header.tis";', open('src/ui/header.tis').read()) \
    .replace('include "file_transfer.tis";', open('src/ui/file_transfer.tis').read()) \
    .replace('include "port_forward.tis";', open('src/ui/port_forward.tis').read()) \
    .replace('include "printer.tis";', open('src/ui/printer.tis').read())

chatbox = open('src/ui/chatbox.html').read()
install = open('src/ui/install.html').read().replace('include "install.tis";', open('src/ui/install.tis').read())

cm = open('src/ui/cm.html').read() \
    .replace('@import url(cm.css);', open('src/ui/cm.css').read()) \
    .replace('include "cm.tis";', open('src/ui/cm.tis').read())


def compress(s):
    s = s.replace("\r\n", "\n")
    x = bytes(s, encoding='utf-8')
    return '&[u8; ' + str(len(x)) + '] = b"' + str(x)[2:-1].replace(r"\'", "'").replace(r'"',
                                                                                  r'\"') + '"'


with open('src/ui/inline.rs', 'wt') as fh:
    fh.write('const _COMMON_CSS: ' + compress(strip(common_css)) + ';\n')
    fh.write('const _COMMON_TIS: ' + compress(strip(common_tis)) + ';\n')
    fh.write('const _INDEX: ' + compress(strip(index)) + ';\n')
    fh.write('const _REMOTE: ' + compress(strip(remote)) + ';\n')
    fh.write('const _CHATBOX: ' + compress(strip(chatbox)) + ';\n')
    fh.write('const _INSTALL: ' + compress(strip(install)) + ';\n')
    fh.write('const _CONNECTION_MANAGER: ' + compress(strip(cm)) + ';\n')
    fh.write('''
fn get(data: &[u8]) -> String {
    String::from_utf8_lossy(data).to_string()
}
fn replace(data: &[u8]) -> String {
    let css = get(&_COMMON_CSS[..]);
    let res = get(data).replace("@import url(common.css);", &css);
    let tis = get(&_COMMON_TIS[..]);
    res.replace("include \\\"common.tis\\\";", &tis)
}
#[inline]
pub fn get_index() -> String {
    replace(&_INDEX[..])
}
#[inline]
pub fn get_remote() -> String {
    replace(&_REMOTE[..])
}
#[inline]
pub fn get_install() -> String {
    replace(&_INSTALL[..])
}
#[inline]
pub fn get_chatbox() -> String {
    replace(&_CHATBOX[..])
}
#[inline]
pub fn get_cm() -> String {
    replace(&_CONNECTION_MANAGER[..])
}
''')
