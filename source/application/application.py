from actions import demo

def main() -> None:
    result = demo.api.simple_demo()
    print(result)
    
if __name__ == '__main__':
    main() 
