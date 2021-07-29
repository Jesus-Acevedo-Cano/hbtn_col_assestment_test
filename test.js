document.addEventListener('DOMContentLoaded', () => {
  dataFn()
})

const dataFn = async () => {
  try {
    const fetchData = await fetch('../../companydb.json')
    const data = await fetchData.json()
    console.log(data)
  } catch (error) {
    console.log(error);
  }
}
