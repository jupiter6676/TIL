package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;


class MemberServiceTest {

    MemberService memberService;
    MemoryMemberRepository memberRepository; // 테스트 데이터 클리어를 위해 가져옴.

    @BeforeEach // 각 테스트 실행 전에 동작
    public void beforeEach() {
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);    // 생성자를 통해 생성하므로, 같은 MemoryMemberRepository를 사용
    }

    @AfterEach  // 메소드가 실행이 끝날 때마다 동작 (콜백 메소드)
    public void afterEach() {
        memberRepository.clearStore();
    }

    @Test
    void 회원가입() {
        // given
        Member member = new Member();
        member.setName("spring");

        // when
        Long saveId = memberService.join(member);

        // then
        Member findMember = memberService.findOne(saveId).get();
        assertThat(member.getName()).isEqualTo(findMember.getName());
        // Assertions.assertThat(member.getName()).isEqualTo(findMember.getName());    // 작성 후, Alt + Enter로 static import
    }

    // join 시 중복 회원 검사를 위해, 테스트에서는 예외를 터뜨리는 것이 더 중요하다.
    @Test
    public void 중복_회원_예외() {
        // given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // when
        memberService.join(member1);
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));// member2가 회원가입할 때 예외가 터져야 함.
        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다."); // 에러 메시지 내용도 검증

//        try {
//            memberService.join(member2);
//            fail("예외가 발생해야 합니다.");  // 이름이 같으므로, 예외가 필연적으로 발생. 발생하지 않으면 실패.
//        } catch (IllegalStateException e) {
//            assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다."); // 다른 메시지를 넣으면 실패
//        }
    }

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }

}