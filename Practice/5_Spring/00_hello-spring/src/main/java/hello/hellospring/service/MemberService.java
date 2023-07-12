package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class MemberService {

    // private final MemberRepository memberRepository = new MemoryMemberRepository();
    private final MemberRepository memberRepository;

    // 생성자 - 외부에서 MemberRepository를 만들도록 설정
    @Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    /** 회원 가입 */
    public Long join(Member member) {
        validateDuplicateMember(member);    // 중복된 이름의 회원은 가입 X
        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        // 드래그 후 Ctrl + Shift + Alt + T로 메소드 추출
        // memberRepository.findByName(member.getName())만 써놓고 Ctrl + Alt + V를 하면 Optional 변수에 저장
        memberRepository.findByName(member.getName())
                        .ifPresent(m -> {   // null이 아닌 값이면, 해당 로직 실행
                            throw new IllegalStateException("이미 존재하는 회원입니다.");
                        });
    }

    /** 전체 회원 조회 */
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }

}
