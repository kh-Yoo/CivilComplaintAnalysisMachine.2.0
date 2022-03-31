package com.jojoldu.book.springboot;

import com.jojoldu.book.springboot.web.storage.StorageService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    CommandLineRunner init(StorageService storageService) {
        return (args) -> {
            //서버 시작시 전체 업로드 경로의 파일 제거
            storageService.deleteAll();
            //파일 업로드 없을 경우 폴더 생성
            storageService.init();
        };
    }
}

