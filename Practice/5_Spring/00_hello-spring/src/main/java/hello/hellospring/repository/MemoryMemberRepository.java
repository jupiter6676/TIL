package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.springframework.stereotype.Repository;

import java.util.*;

/**
 * 동시성 문제가 고려되어 있지 X, 실무에서는 ConcurrentHashMap, AtomicLong 사용 고려
 */
public class MemoryMemberRepository implements MemberRepository {

    private static Map<Long, Member> store = new HashMap<>();   // id-Member
    private static long sequence = 0L;  // key 값 생성

    @Override
    public Member save(Member member) { // member의 name은, 회원이 입력해서 넘어온 상태
        member.setId(++sequence);       // id는 시스템에서 설정
        store.put(member.getId(), member);

        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny(); // store의 값들(Member) 중, name과 같은 것이 하나라도 있으면 반환
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values());
    }

    public void clearStore() {
        store.clear();
    }

}
