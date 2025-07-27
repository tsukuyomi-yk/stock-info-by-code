document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('code');
  const button = document.getElementById('search');
  const result = document.getElementById('result');

  let stockData = {};

  async function loadData() {
    try {
      const res = await fetch('stock_data.json');
      stockData = await res.json();
    } catch (e) {
      result.innerHTML = '<p>データの読み込みに失敗しました。</p>';
    }
  }

  function display(code) {
    const data = stockData[code];
    if (!data) {
      result.innerHTML = '<p>該当するデータが見つかりません。</p>';
      return;
    }
    if (data.error) {
      result.innerHTML = `<p>${data.name} の取得に失敗しました: ${data.error}</p>`;
      return;
    }

    result.innerHTML = `
      <p><strong>${data.name}</strong></p>
      <p>株価: ${data.price} 円</p>
      <p>前日比: ${data.change >= 0 ? '+' : ''}${data.change} 円 (${data.percent}%)</p>
      <p>更新日時: ${new Date(data.updated).toLocaleString()}</p>
    `;
  }

  button.addEventListener('click', () => {
    display(input.value.trim());
  });

  input.addEventListener('keypress', e => {
    if (e.key === 'Enter') display(input.value.trim());
  });

  loadData();
});
