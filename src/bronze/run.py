from .processor import build_bronze


if __name__ == '__main__':
    counts = build_bronze()
    print('BRONZE BUILD COMPLETE')
    for dataset, count in counts.items():
        print(f'{dataset}: {count}')
