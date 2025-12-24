def main():
    
    # importar ambas as bibliotecas pandas e matplotlib
    # o pandas para leitura dos dados e o matplotlib para a vizulização dos gráficos
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # o comando pd.read_csv para fazer a leitura dos dados
    df_nba_stats = pd.read_csv("nba_player_stats.csv")
    
    # cria-se uma nova variaqvel para definir quais elemtn
    df_ppg = df_nba_stats["PPG"]
    
    plt.hist(df_ppg)
    plt.show()
    
if __name__ == "__main__":
    main()