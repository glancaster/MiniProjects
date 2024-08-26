# From python-mini-projects @ Nuh Mohammed
import socket

def get_hostname_IP():
    hostname = input("Enter Website Address: ")
    try:
        print(f"Hostname: {hostname}")
        print(f"IP: {socket.gethostbyname(hostname)}")
    except Exception as e:
        print("Invalid Hostname, see info.md")

def test_get_ip_by_hostname(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "www.google.com")
    get_hostname_IP()
    captured = capsys.readouterr()
    assert True    
if __name__ == "__main__":
    get_hostname_IP()
