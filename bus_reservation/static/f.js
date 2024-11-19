document.getElementById("search-button").addEventListener("click", function() {
    // 사용자 입력 값 가져오기
    const departure = document.getElementById("departure").value;
    const destination = document.getElementById("destination").value;
    const departureDate = document.getElementById("departure-date").value;
    const departureTime = document.getElementById("departure-time").value;

    // 간단한 유효성 검사
    if (!departure || !destination || !departureDate || !departureTime) {
        alert("Please fill in all fields.");
        return;
    }

    // 다음 단계로 이동할 준비가 되었다는 메시지
    alert(`Searching buses from ${departure} to ${destination} on ${departureDate} at ${departureTime}.`);

    // 실제로는 여기에서 백엔드 API에 데이터를 보내거나 다음 단계로 이동
});
