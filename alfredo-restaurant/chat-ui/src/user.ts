export function getUserInfo() {
    const ids: number[] = [1234, 5678, 9101];
    const randomIndex = Math.floor(Math.random() * ids.length);
    return ids[randomIndex];
}
